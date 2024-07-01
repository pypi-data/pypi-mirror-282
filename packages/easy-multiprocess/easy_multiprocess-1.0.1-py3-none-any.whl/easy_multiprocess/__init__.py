import sys
if sys.platform == 'win32':
    raise OSError("This package does not support Windows.")

from .easy_multiprocess import *
__version__ = "1.0.0"
