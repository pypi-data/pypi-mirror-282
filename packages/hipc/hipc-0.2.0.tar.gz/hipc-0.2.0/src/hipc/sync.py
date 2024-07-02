from datetime import datetime
from functools import reduce
import json
import os
from os.path import expandvars as expand
from os.path import join as pjoin
from pathlib import Path
import pickle
import subprocess
import shutil
from subprocess import PIPE
import time
from tqdm import tqdm
import warnings

from hipc.env import EnvTree

PORTFILE = "port.json"

class Port(object):
    """HPC port object. Sync source code and data, pass python functions
    through here and have them execute on a remote machine.
    
    Args:
        directory (str): The path of the HPC source directory to sync with,
            relative to the home directory. Serves as a name for this port/environment.
        user (str): HPC username.
        host (str): HPC host domain name.
        build (bool): Option to build python environment on HPC.
    """
    def __init__(self, directory, user, host, build=True):
        #: (str) The relative path of the HPC source directory.
        self.directory = directory
        #: (str) The user name on the HPC machine.
        self.user = user
        #: (str) The full domain name of the host machine.
        self.host = host
        #: (str) The account + host domain string
        self.account = user + "@" + host
        #: (bool) Option to build environment.
        self.build = build 

        # Get remote base directory for this port, default is $HOME.
        self.remote_base = ""
        self._env_path = ""
        if host:
            self.remote_base = self.get_remote_home()
            self._env_path = pjoin(self.remote_base, self.directory)

        # Groups of source files to be synced with HPC
        self.src_paths = {}

        #: Store the scratch directory associated with this machine, default
        # to remote home.
        self.scratch_dir = self.remote_base

        # Option to install conda requirements in HPC env
        self.requirements = False

        # By default, add local python files
        self.match_src()

        #: (str) Conda channel to install dependencies.
        self.channel = None

        #: HPC modules required for environment setup
        self.env_modules = []
        self.add_module("python")

        #: Slurm options
        self.slurm_config = {}

        #: Download option
        self.download_paths={}

    def set_directory(self, directory):
        self.directory = directory
        self._env_path = pjoin(self.remote_base, self.directory)


    def upload(self, options="a", dryrun=False, delete=False, verbose=False):
        """Upload source files and data to the HPC machine.

        Args:
            options (str): rsync options.
                Default is ``"a"``.
            dryrun (bool): rsync dry run.
            delete (bool): Option to delete files at destination that are no
                longer in source.
            verbose (bool): Set verbosity level to ``v``, ``vv``, or ``vvv``.
        """
        drystr = "--dry-run" if dryrun else ""
        dest_str = f"{self.account}:{self._env_path}"

        vstr = "-"+verbose if verbose else ""

        # Establish base dir through ping since old version of rsync (likely on HPC)
        # does not implement --mkpath
        self.establish_dir(delete=delete)
        if self.scratch_dir != self.remote_base:
            self.establish_dir(scratch=True, delete=delete)

        for root, f in self.src_paths.items():

            efinal = f"--exclude='**' \\\n" # baseline exclusion

            in_, ex_ = f["include"], f["exclude"]
            if root != ".":
                root_base = Path(root).parts[-1]
                exclude = [pjoin(root_base, e) for e in ex_]
                include = [pjoin(root_base, e) for e in in_]
                efinal = f"--exclude='{pjoin(root_base, '**')}' \\\n"

            estr = "".join(f"--exclude='{exc}' \\\n" for exc in ex_)
            istr = "".join(f"--include='{inc}' \\\n" for inc in in_)
            filters = estr + istr + efinal

            if verbose: print(f"rsync -{options} {vstr} \\\n{filters}{drystr} "
                              f"\\\n{root} {dest_str}")
            os.system(f"rsync -{options} {vstr} \\\n{filters}{drystr} "
                              f"\\\n{root} {dest_str}")

    def download(self, options="a", verbose=False):
        """Download data files from HPC to the local environment."""
        dest_str = "."
        vstr = "-"+verbose if verbose else ""

        # Down sync port from server
        hpc_port_path = pjoin(self._env_path, PORTFILE)
        os.system(f"rsync {self.account}:{hpc_port_path} {PORTFILE}")
        self.load(PORTFILE)

        # Make local directory
        os.makedirs(self.directory, exist_ok=True)
        
        
        efinal = f"--exclude='**' \\\n" # baseline exclusion

        # XXX: untest case of naming collisons across roots
        for root, dlist in self.download_paths.items():
            root_base = Path(root).parts[-1]
            include = [pjoin(root_base, e) for e in dlist]
            efinal = f"--exclude='{pjoin(root_base, '**')}' \\\n"
            istr = "".join(f"--include='{inc}' \\\n" for inc in include)
            filters = istr + efinal

            src_str = f"{self.account}:{root}"

            if verbose: print(f"rsync -{options} {vstr} \\\n{filters} "
                              f"\\\n{src_str} {dest_str}")
            os.system(f"rsync -{options} {vstr} \\\n{filters} "
                              f"\\\n{src_str} {dest_str}")


    def mirror(self, path="."):
        """Distribute the build environment to a new path in the scratch
        directory.

        Args:
            path (str): The path of the new environment relative to
            /.../<scratch root>/<port name>/.
        """
        source = self._env_path
        dest_root = pjoin(self.scratch_dir, self.directory)
        dest = pjoin(dest_root, path)
        os.makedirs(dest_root, exist_ok=True)
        shutil.copytree(source, dest, dirs_exist_ok=True)

    def establish_dir(self, scratch=False, delete=False):
        """Create a directory relative to home or the scratch dir.

        Args:
            scratch (bool): Use scratch dir as base.
            delete (bool): Delete the contents of the directory before making it.
        """

        if scratch: abs_path = pjoin(self.scratch_dir, self.directory)
        else: abs_path = self._env_path
        args = ["ssh", self.account, "mkdir", "-p", abs_path]
        subp_pipe(args, v=False, verr=False)
        if delete and input(f"***DELETE*** the contents of {abs_path} on {self.host}? (y/n): ") == "y":
            args = ["rm", "-r", pjoin(abs_path, "*")]
            subp_pipe(args, v=False, verr=False)

    def killjobs(self):
        """Cancel all jobs associated with this HPC connection."""
        # TODO
        pass

    def execute(self, executable, idev=False):
        """Execute a shell command over the HPC port in the environment directory.

        Args:
            executable (str): command to run from HPC shell.
            idev (bool): Whether or not to run from an interactive compute node
                (must use tmux before entering interactive job).
        """

        mods = " ".join(self.env_modules)
        if idev:
            # Start an MPI interactive job in a tmux session. Access the
            # environment on host with tmux or other server.
            args = ["ssh", self.account, (
                f"tmux send \"source /etc/profile; "
                f"&& cd {self._env_path} && {executable}\" Enter")]
        else:
            args = ["ssh", self.account, (
                f"module load {mods}  && cd {self._env_path} && "
                f"{executable}")]
        # Run the process and pipe output back to stdin continuously
        interactive_subprocess(args)

    def deploy(self, executable, idev=False, download=False):
        """Sync source code and send a command line execution to the HPC machine.

        Args:
            executable (str): command to run from HPC shell
            idev (bool): Whether or not to run from an interactive compute node
                (must use tmux before entering interactive job).
            download (bool) Download files from HPC after running command.
        """
        # Dump port params
        self.dump()
        self.match_src(include="port.json")
        self.upload()
        self.execute(executable, idev=idev)
        if download: self.download()

    def __call__(self, module, function=None, interactive=False, download=True):
        """Call a python function on the HPC machine.

        Args:
            module (str): Name of a python module available in the environment.
            function (str): Name of a function to call from HPC which accepts
                no arguments.
        """
        if function is None:
            e = f"python {module.replace('.py', '')}.py"
        else:
            e = f"python -c \'import {module};{module}.{function}()\'"

        if self.requirements:
            if self.build:
                e = f"pip install hipc; {self.channel} install -r {self.requirements}; {e}"
        self.deploy(e, idev=interactive, download=download)

    def add_module(self, mods):
        """Add a module to home node environment.

        Args:
            mods (str or list): The modules to be imported via ``module load ...``
        """
        mods = ensure_list(mods)
        self.env_modules += mods

    def get_remote_home(self):
        """Find the home directory on the remote server."""
        args = ["ssh", "-tt", self.account, "echo \"__remote_home_slug\"; pwd"]
        lines = subp_pipe(args, v=False, verr=False)

        if not len(lines): return ""
        remote_home = lines[lines.index("__remote_home_slug")+1]
        return remote_home

    def scratch(self, path):
        """Use the scratch directory instead of the home directory."""
        self.scratch_dir = path

    def match_src(self, include="**.py", exclude=None, root="."):
        """Include and exclude source files for sync operation.

        Args:
            root (callable[str]): A local base directory to export from.
            include (str or list): Include pattern or list of patterns relative to root.
                By default, recursively include python files.
            exclude (str or None): Exclude files matching pattern even if they are 'included'.
        """
        if exclude is None: exclude = []
        exclude = ensure_list(exclude)
        include = ensure_list(include)

        if root not in self.src_paths:
            self.src_paths[root] = {"include": include, "exclude": exclude}
        else:
            rt = self.src_paths[root]
            rt["include"] += include
            rt["exclude"] += exclude
            # No duplicates necessary
            rt["include"] = sorted(list(set(rt["include"])))
            rt["exclude"] = sorted(list(set(rt["exclude"])))

    def add_py_dependencies(self, path, channel="pip"):
        """Add python requirements file."""
        self.match_src(path)
        self.requirements = path
        self.channel = channel

    def dump(self, in_hpc=False):
        """Store port information into json file."""
        # Don't need private members
        public = {k: v for k, v in self.__dict__.items()
                  if not k.startswith("_")}

        if in_hpc: p = pjoin(self._env_path, PORTFILE)
        else: p = PORTFILE
        with open(p, "w") as f:
            json.dump(public, f, indent=4, separators=(",", ": "))

    def load(self, path=None):
        """Load port information from json file."""
        if path is None: load_file = pjoin(self._env_path, PORTFILE)
        else: load_file = path

        if not os.path.exists(load_file): return None
        with open(load_file, "r") as f:
            d = json.load(f)
            for k, v in d.items(): setattr(self, k, v)

        # Update env path
        self._env_path = pjoin(self.remote_base, self.directory)
        return self

    def apply(self, f, *args, kwargs=None, scratch=True, v=False,
              match=None, save=False, local=False):
        """Apply a callback function to a set of calculations."""

        if scratch: abs_path = pjoin(self.scratch_dir, self.directory)
        else: abs_path = self._env_path

        if kwargs is None: kwargs = {}

        callbacks = [(f, args, kwargs)]

        tree = EnvTree(abs_path)
        res = list(tree.traverse(match, callbacks=callbacks, v=v))

        if save:
            name = f.__name__+".pckl"
            path = pjoin(abs_path, name)

            print(res)
            with open(path, "wb") as f:
                pickle.dump(res, f)
            if abs_path not in self.download_paths:
                self.download_paths[abs_path] = [name]
            else:
                self.download_paths[abs_path].append(name)
            # TODO: Flag?
            self.dump(in_hpc=not local)

        return res


def subp_pipe(args, v=True, verr=True):
    """Run the process and pipe output back to stdin continuously."""
    p = subprocess.Popen(args, stdout=PIPE, stderr=PIPE)
    stdout = []
    while not p.poll():
        line = p.stdout.readline().decode().rstrip()
        if not line: break
        if v: print(line, flush=True)
        stdout.append(line)
    err = "".join(s.decode() for s in p.stderr.readlines())
    if err and verr: warnings.warn(err, RuntimeWarning)
    return stdout

def interactive_subprocess(args, tee=True, std_buf=None,
                           err_buf=None, callbacks=None):
    """Open a subprocess and pipe the output back to the parent.
    Optionally allow for 'tee'-like behavior and also print out process
    stdout at the same time."""

    if callbacks is None: callbacks = []

    # Start process in simulation directory
    p = subprocess.Popen(
        args, bufsize=1, universal_newlines=True,
        stdout=PIPE, stderr=PIPE)

    # Ensure file reading doesn't wait for subprocess to close when
    # sending updates
    os.set_blocking(p.stdout.fileno(), False)

    if std_buf: f = open(std_buf, "w", buffering=1)

    def run_callbacks():
        lines = p.stdout.readlines()
        txt = "".join(lines)
        if std_buf: f.write(txt)
        if callbacks: [c() for c in callbacks]
        if tee: print(txt, end="", flush=True)

    while p.poll() is None:
        # Release lock to the subprocess if running
        # on one core.
        time.sleep(2)
        run_callbacks()

    # Run buffering one last time.
    run_callbacks()

    if std_buf: f.close()

    # Log errors into .err file after failure and raise
    # as warning in the parent
    err = p.stderr.readlines()
    if err_buf:
        with open(err_buf, "w") as e:
            e.write("\n".join(err))
    elif err:
        warnings.warn("".join(err), RuntimeWarning)

    return p

def ensure_list(x):
    if not isinstance(x, list): return [x]
    else: return x

def read(path=None):
    """Create a new Port object from a json file."""
    if path is None: path = pjoin(os.getcwd(), PORTFILE)
    p = Port("", "", "")
    p.load(path)
    return p
