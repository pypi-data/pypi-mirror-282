"""Use a tag based system to recover file identities."""
from datetime import datetime
import os
from os.path import join as pjoin
from pathlib import Path

MAX_SERVE = 1000

class EnvTree():
    """Environment manager for tests on HPC machines. It is usually desirable to
    create a new environment (directory) for every calculation that has a different
    set up inputs. This object makes it easy to create new trees of tests, make them
    searchable, and have them intereact with HPC job managers to determine if it is safe
    to change data in the tree.

    Args:
        root (str): The base path of the environment.
        interactive (bool): Option for stdin tag queries (NYI).
    """

    def __init__(self, root=".", interactive=False, layers=1, callback=None):
        #: (str) The abolute root path of this tree
        self.root = root
        #: Store associate tags
        self.tag_map = {}

        self.index = 1
        #: (int): The depth of the physical environment tree
        self.layers = layers


    def create_env(self, p=None, callback=None):
        callback = ensure_list(callback) if callback is not None else []
        # For now, independent of p
        ts = datetime.now().date()
        subdir = f"{self.index} {ts}".replace(" ", "_")
        with visit(self.root):
            os.makedirs(subdir, exist_ok=True)
            self.tag(subdir)
            for cb in callback: cb(subdir)
        return subdir

    def tag(self, path):
        with open(pjoin(path, ".env_tags"), "w") as f:
            f.write("")

    def traverse(self, match=None, callbacks=None, v=False):
        """Apply callbackss to every directory and yield their results."""

        callbacks = ensure_list(callbacks) if callbacks is not None else []
        # For now, just use physical dirs regardless of tags.
        for (ps, ds, _) in os.walk(self.root):
            for d in ds:
                path = pjoin(ps, d)
                if not match(Path(path).resolve()): continue
                if v: print(path, flush=True)
                with visit(path):
                    results = []
                    for cb in callbacks:
                        if isinstance(cb, tuple):
                            results.append(cb[0](*cb[1], **cb[2]))
                        else:
                            results.append(cb())
                    yield results

    def serve(self, cd=False):
        for i in range(MAX_SERVE):
            e = self.create_env()
            self.index += 1
            if cd:
                with visit(pjoin(self.root, e)):
                    yield e
            else: yield e

        raise RuntimeError(f"Max environment number served: {MAX_SERVE}")


class TestNode():
    """Tree based tag system"""
    # TODO
    def __init__(self, path, p=None):
        pass

class visit(object):
    """Directory environment context manager."""
    def __init__(self, path):
        self.original_path = os.getcwd()
        self.path = path

    def __enter__(self):
        os.chdir(self.path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.original_path)

def ensure_list(x):
    if not isinstance(x, list): return [x]
    else: return x
