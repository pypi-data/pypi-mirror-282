import copy
from functools import reduce
import inspect
import json
import multiprocessing as mp
import pickle
import os
from os.path import join as pjoin
from pathlib import Path
import re
import shlex
import subprocess
import time
import warnings

import hipc
from hipc.sync import Port
from hipc.env import EnvTree
from hipc.env import visit
import numpy as np
import pandas as pd

class Parameters(object):
    """A struct of parameters which can also be indexed / iterated
    like a dictionary. The intended use is to create a set of
    parameters with a unique set of easy to remember keys with readable
    values (numbers, strings, not collections and general objects).

    Args:
        filename (str): The file name of the parameter save.
    """

    def __init__(self, p={}):
        #: (set) Named tags that apply to this parameter set.
        self._tags = set() # TODO: implement
        self.set(p)

    def __index__(self, s):
        return getattr(self, s)

    def map(self):
        """Return the set of parameters and their default values
        as a python dictionary."""
        m = {k: v for k, v in inspect.getmembers(self)
                if not k.startswith("_") and not callable(v)}
        return m

    def tag(self, tags):
        """Add a tag, or set of tags so this set of parameters can be
        searchable for later.

        Args:
            tags (str, or set[str]): The tags that apply to this set of
            parameters.
        """
        if not isinstance(tags, set): tags = {tags}
        self._tags = self._tags.union(tags)

    def set(self, p):
        """Take a dictionary or parameters object of values and set the corresponding
        attributes of this object.

        Args:
            p (dict or :class:`~.hipc.job.Parameters`): A collection of settings
                apply to this set of parameters.
        """
        if isinstance(p, Parameters): p = p.map()
        for k, v in p.items(): setattr(self, k, v)

    def write(self, fname="parameters.json"):
        """Store parameters to file in a human readable format."""
        with open(fname, "w") as f:
            json.dump(self.map(), f, indent=4)

    def read(self, fname="parameters.json"):
        """Read in parameters from json file."""
        with open(fname, "r") as f:
            d = json.load(f)
        self.set(d)

    def pretty(self, a):
        """Optional pretty print mapping for each param."""
        pass

    def __repr__(self):
        with pd.option_context("display.float_format", "{:.6e}".format):
            s = pd.Series(self.map()).__repr__()
        s = "\n".join(s.split("\n")[:-1])
        return s

class Calculator(object):
    """Interface for any kind of calculation that is run-able
    and depends on dynamics parameters can be compatible with multiprocessing
    utilities like SlurmManager and DistributedPool."""

    def get(self):
        """Return the current state of parameters.

        Returns:
            (``~.hipc.job.Parameters): The current ``Parameters`` state.
        """
        raise NotImplementedError("Calculator must implement get(self) method.")

    def set(self, **state_options):
        """Update the internal state of the object being run.

        Args:
            **state_options: Keywords arguments corresponding to attributes of the object
                being updated.
        """
        raise NotImplementedError("Calculator must implement set(self, **state_options) method.")

    def run(self, **run_options):
        """Run the calculation with the current settings.

        Args:
            **run_options: Keywords arguments that modify the nature of the
                way the program runs.
        """
        raise NotImplementedError("Calculator must implement run(self, **run_options) method.")

    def set_ncores(self, ncores):
        """Option to set the number of cores to be used in each runner call.
        This is only required for use in the SLURM manager.

        Args:
            ncores (int): The number of cores.
        """
        raise NotImplementedError("Calculator must implement set_ncores(self, ncores) method.")

    def set_directory(self, path):
        """Set the directory of the calculation environment.

        Args:
            ncores (int): The number of cores.
        """
        raise NotImplementedError("Calculator must implement set_directory(self, path) method.")


class DistributedPool(object):
    """A multiprocessing Pool context for running
    calculations among cores with different settings. Either pass a base directory
    to host all the calculation environments or include directory specifications
    within the ``Calculator`` parameter space.

    Args:
        runner (Calculator): The calculation runner.
        processes (int): The number of cores to divide up the work.
        path server (str): Path to calculation root (optional).
    """

    def __init__(self, runner: Calculator, processes=None):
        # Always use the fork context
        mpc = mp.get_context("fork")
        self.runner = runner
        self.pool = mpc.Pool(processes=processes)
        self.server = EnvTree().serve()

    def submit(self, run=None, cores=None, **set_args):
        """Submit a single job with updated key words to the pool.

        Args:
            run (dict): Keyword arguments to be passed to
                :meth:`~.hipc.job.Calculator.run`.
            cores (int): The number of cores to use in this run call.
            **set_args: Keyword arguments passed to
                :meth:`~.hipc.job.Calculator.set`
                before calling :meth:`~.hipc.job.Calculator.run`.
        """
        if run is None: run = {}
        # Copy the state of the runner (this ensures that
        # the parameter state does not get overwritten while
        # the processors are all busy)
        self.runner_child = copy.deepcopy(self.runner)
        # Keyword args will be sent to the set function
        self.runner_child.set(**set_args)
        if cores: self.runner_child.set_ncores(cores)
        # Get environment in new base directory
        self.pwd = next(self.server)
        self.runner_child.set_directory(self.pwd)
        # run args are sent separately with the caller
        self.pool.apply_async(
            self.runner_child.run, (), run,
            error_callback=self.err_callback)

    def __enter__(self):
        """Pipe the context input back to caller."""
        self.pool.__enter__()
        return self

    def err_callback(self, err):
        """Print out errors that subprocesses encounter."""
        warnings.warn(f"Error in process: PID={os.getpid()} "
                      f"path={self.pwd}\n\n{str(err)}", RuntimeWarning)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Safely wait for all processes to finish and exit the pool."""
        # Stop accepting jobs
        self.pool.close()
        # Wait for all jobs to finish
        self.pool.join()
        # Terminate multiprocessing pool
        self.pool.__exit__(exc_type, exc_val, exc_tb)

class SlurmManager(object):
    """A python context interface for the common Slurm HPC job manager
    to run more several intensive calculations on large clusters.
    See https://slurm.schedmd.com/sbatch.html.

    Args:
        runner (Calculator): The calculation runner.
        directory (str or None) The simulation directory. Default is
            the current working directory. If not provided a
            :class:`~.hipc.sync.Port` file will be queried for the
            base scratch environment. If not found, the current
            directory will be used.
        modules (list[str]): A list of modules to be loaded by the
            HPC module system.
        mock (bool): Option to test scripts without calling a slurm
            manager.
        **options: Additional keyword arguments will be interpreted as
            SLURM parameters.

    Note:
        This job manager currently only works for clusters that either
        already have the gcc and python requirements installed on each
        compute node, or clusters that use the
        `Module System <https://hpc-wiki.info/hpc/Modules>`_ to load
        functionality.
 
        The default behavior is to accommodate the module system as it
        is common on most HPC machines. If you wish to avoid writing
        ``module load`` commands in the SLURM script, simply specify
        ``modules=[]`` in the constructor.
    """
    modules = ["python", "gcc"]
    _pckl_file = "job.pckl"

    def __init__(self, runner: Calculator, directory=None,
                 modules=["python", "gcc", "openmpi"], mock=False, **options):

        self.port = None
        if directory is None:
            # Check for port config
            self.port = hipc.sync.read()
            if self.port is None:
                directory = os.getcwd()
            else:
                directory = pjoin(self.port.scratch_dir, self.port.directory)
        # Make group directory absolute
        if not os.path.isabs(directory):
            directory = str(Path(directory).resolve())
        #: The simulation directory
        self.directory = directory
        #: The list of modules to be loaded by the HPC module system.
        self.modules = modules
        #: The :class:`~.hipc.job.Calculator` object.
        self.runner = runner
        # Option to test the scripts without calling a slurm manager
        self.mock = mock
        # These will hold all the updates to both slurm and the runner
        self.input_sets = []
        #: Store references to the slurm job numbers after jobs are submitted
        self.job_ids = []
        #: The SLURM sbatch options
        self.options = slurm_defaults().copy()
        if self.port: self.set(**self.port.slurm_config) # Add port defaults
        self.set(**options)
        #: Initialize directory / environment generator

        # Make sure cores are specified
        msg = (f"{self.__class__.__name__} requires "
                "the number of cores available at each node "
                "to be passed as ntasks-per-node.")
        if not "ntasks-per-node" in self.options:
            raise RuntimeError(msg)
        if not self.options["ntasks-per-node"]:
            raise RuntimeError(msg)

        # Initialize directory server
        self.env_server = EnvTree(
            self.directory, callback=self.port.mirror).serve(cd=True)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit and run sbatch for all the inputs."""
        # Number of input sets
        nsubs = len(self.input_sets)
        subs_remaining = nsubs
        nsubbed = 0
        while subs_remaining:
            # Distribute cores into minibatches
            ntasks = self.input_sets[nsubbed]["_slurm"]["ntasks-per-node"]
            cores_remaining = ntasks
            minibatch_inputs = []
            while cores_remaining:
                nset = self.input_sets[nsubbed]
                if nset["_ncores"] == "all": nset["_ncores"] = ntasks
                next_cores = nset["_ncores"]
                if cores_remaining >= next_cores:
                    # Add to minibatch
                    minibatch_inputs.append(nset)
                    cores_remaining -= next_cores
                    nsubbed += 1
                    subs_remaining -= 1
                else:
                    # Subtract remaining cores from SLURM request.
                    ntasks -= cores_remaining
                    break

            # Consolidate slurm settings across jobs
            slurm_input = self.merge_slurm(minibatch_inputs)
            # Update node request if necessary
            slurm_input["ntasks-per-node"] = ntasks

            # Take any slurm updates from first input
            self.set(**slurm_input)

            # Pickle the runner class and inputs, then in batch script,
            # construct object, set, run
            # Create new compute node environment
            next(self.env_server)

            # Write runner class pickle the node directory level
            with open(self._pckl_file, "wb") as f:
                pickle.dump((minibatch_inputs, self.runner.__class__), f)

            # Write the slurm script
            self.write_slurm_script()
            # Execute slurm call
            self.sbatch()

    def merge_slurm(self, inputs):
        """Take a list of input dictionaries and return a single
        merged copy.

        Args:
            inputs (list[dict]): A list of parameter settings to be
                merged.
        
        Returns:
            (dict): The merged SLURM parameters.
        """
        i0 = inputs[0]["_slurm"]
        # For now, just prevent most quantities from changing
        changed = {}
        for k, v in i0.items():
            changed = reduce(lambda a, b: a if a == b else "_changed",
                             [m["_slurm"][k] for m in inputs])
            if k != "time" and changed == "_changed":
                raise RuntimeError(f"SLURM setting '{k}' "
                    "changed within a single sbatch job.")

        # Take max of time
        tmax = max(m["_slurm"]["time"] for m in inputs)
        i0["time"] = tmax
        return copy.deepcopy(i0)


    def submit(self, run=None, slurm=None, ncores="all", **settings):
        """Add a set of parameter updates to the job queue.
        Slurm is not invoked until the context is exited.

        Args:
            run (dict): Keyword arguments to be passed to
                :meth:`~.hipc.job.Calculator.run`.
            slurm (dict): Keyword arguments to be passed to the
                SLURM manager.
            ncores (int or str): Set a specific number of cores for this job.
                Default is ``"all"``, which will use
                all the cores available to the sbatch invocation as determined
                by the ``ntasks-per-node`` SLURM option.
            **settings: Keyword arguments passed to the
                :meth:`~.hipc.job.Calculator.set`.
                before calling :meth:`~.hipc.job.Calculator.run`.
        """
        if run is None: run = {}
        if slurm is None: slurm = {}

        self.set(**slurm)

        combined_settings = {
            "_run": run, "_slurm": copy.deepcopy(self.options),
            "_ncores": ncores
        }

        combined_settings.update(self.runner.get().map())
        combined_settings.update(**settings)
        self.input_sets.append(combined_settings.copy())

    def sbatch(self):
        """Call slurm with current settings."""
        if self.mock:
            # Just call the script and block
            self.mock_run()
            return
        # Otherwise, submit to slurm
        cmds = ["date | tee -a jobnum", "sbatch job_script.sh | tee -a jobnum"]
        subprocess.run(cmds[0], shell=True)
        sub_string = subprocess.check_output(cmds[1], shell=True).decode()
        if not len(sub_string): return
        self.job_ids.append(int(sub_string.split()[-1]))

    def set(self, **options):
        """Update slurm manager options.

        Args:
            **options: :class:`~.hipc.job.Parameters` settings.
        """
        # Ensure there is no naming collision between
        # ``Parameters`` settings and SLURM settings
        self.options.update({k:v
            for k, v in options.items()
            if k in slurm_defaults()})

    def write_slurm_script(self, path=None, script_name=None):
        """Write the SLURM batch script."""
        if script_name is None:
            script_name = "job_script.sh"
        if path is None:
            path = os.getcwd()
        with open(pjoin(path, script_name), "w") as f:
            f.write("#!/bin/bash\n")
            for k, v in self.options.items():
                if not v:
                    continue
                f.write(f"#SBATCH --{k}={v}\n")

            if not self.mock:
                # Only load modules if this is a real slurm run
                f.write("\n")
                for mod in self.modules:
                    f.write(f"module load {mod}\n")
                f.write("\n\n")

            python_script = self.process_batch_script()
            # Declare pyscript var
            f.write("SCRIPT=$(cat<<END\n")
            f.write(python_script)
            f.write("END\n")
            f.write(")\n\n")
            f.write("python -c \"$SCRIPT\"\n")

    def process_batch_script(self):
        """Inspect the batch script below and process it for use
        in sbatch."""
        source = inspect.getsource(self.batch_script)
        source = "\n".join(source.split("\n")[4:])
        # Inject pckl name
        source = source.replace("self._pckl_file", f"\"{self._pckl_file}\"")
        # Remove indents
        source = re.sub(r"^[^\S\n]{8}", "", source, flags=re.MULTILINE)
        return source

    def batch_script(self):
        """The SLURM job script. This does not get called in the
        parent process, but instead the source code is invoked in the
        sbatch script/command for subprocess startup."""
        import pickle
        from hipc.job import DistributedPool
        from hipc.env import EnvTree
        # Load in batch parameters
        with open(self._pckl_file, "rb") as f:
            updates, Runner = pickle.load(f)
        # Construct runner
        runner = Runner()
        # Run settings through distributed processing interface
        with DistributedPool(runner, processes=len(updates)) as pool:
            for update in updates:
                # Separate submit args
                exclude = {"_slurm", "_ncores"}
                submit_args = {k: v for k, v in update.items()
                    if k not in exclude}
                # Submit
                pool.submit(run=update["_run"], cores=update["_ncores"], **submit_args)

    def mock_run(self):
        """Act as a compute node and test the job scripts sequentially."""
        os.system(f"chmod +x job_script.sh")
        os.system(f"./job_script.sh")

    def has_active(self):
        """Check whether any submitted jobs are still pending or running.

        Returns:
            (bool): ``True`` if there are still jobs that are pending or
                running. ``False`` otherwise.
        """
        has_active = False
        for job_id in self.job_ids:
            is_active = False
            try:
                cmd = f"scontrol show job {job_id}"
                sub_string = subprocess.check_output(
                    shlex.split(cmd)).decode()
                is_active = "PENDING" in sub_string or "RUNNING" in sub_string
            except subprocess.CalledProcessError as e:
                is_active = False
            has_active = has_active or is_active
        return has_active

    def has_pending(self):
        """Check whether any submitted jobs are still pending.

        Returns:
            (bool): ``True`` if there are still jobs that are pending.
                ``False`` otherwise.
        """
        has_pending = False
        for job_id in self.job_ids:
            is_active = False
            try:
                cmd = f"scontrol show job {job_id}"
                sub_string = subprocess.check_output(
                    shlex.split(cmd)).decode()
                is_pending = "PENDING" in sub_string
            except subprocess.CalledProcessError as e:
                is_pending = False
            has_pending = has_pending or is_pending
        return has_pending

    def join(self):
        """Wait for all slurm jobs to finish."""
        while self.has_active():
            time.sleep(2)

#: SLURM parameters
def slurm_defaults():
    return {
        # The HPC user account
        "account": None, # required
        "job-name": None, # required
        "ntasks-per-node": None, # required, number of cores in each compute node
        "qos": None, # Quality of service
        "reservation": None, # Request particular resources
        "partition": None, # Request a specific partition
        "time": 60, # job minutes
        "array": None, # option for multi-task submission.
        "bb": None, "bbf": None, # burst buffer
        "begin": None, # scheduled runtime
        "chdir": None, # working directory of cluster process
        "clusters": None, # comma separated string of clusters
        "comment": None, # slurm script comment
        "constraint": None, # more constraints
        "deadline": None,
        "error": "job.err",
        "output": "job.out",
        "mail-user": None,
        "mail-type": None,
        # name / cpu / task / node allocation left to Manager
    }
