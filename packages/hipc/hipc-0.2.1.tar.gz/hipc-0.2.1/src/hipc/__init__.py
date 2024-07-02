# read version from installed package
from importlib.metadata import version
__version__ = version("hipc")

from .job import Parameters
from .job import Calculator
from .job import DistributedPool
from .job import SlurmManager
from .sync import Port
from .sync import read

