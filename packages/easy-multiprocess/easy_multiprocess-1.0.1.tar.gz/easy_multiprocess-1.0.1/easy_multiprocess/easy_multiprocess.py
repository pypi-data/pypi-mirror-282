
from concurrent.futures import ProcessPoolExecutor
import atexit
import functools
import os

# change default start method to fork
import multiprocessing
multiprocessing.set_start_method('fork')

class ProcessPoolManager:
    _process_pool = None
    _debug = False
    _max_workers = None

    @classmethod
    def get_executor(cls):
        if cls._process_pool is None:
            if cls._max_workers:
                cls._process_pool = ProcessPoolExecutor(max_workers=cls._max_workers)
            else:
                cls._process_pool = ProcessPoolExecutor()
            atexit.register(cls.cleanup)
        return cls._process_pool

    @classmethod
    def set_max_workers(cls, max_workers):
        cls._max_workers = max_workers
        cls.recreate_executor()
    
    @classmethod
    def recreate_executor(cls):
        cls.cleanup()
        cls.get_executor()

    @classmethod
    def cleanup(cls):
        if cls._process_pool is not None:
            cls._process_pool.shutdown()

        cls._process_pool = None

function_registry = dict()
def execute_from_registry(func_name, *args, **kwargs):
    os.environ["INSUBPROC"] = "True"
    func = function_registry[func_name]
    return func(*args, **kwargs)

def parallelize(func):
    ProcessPoolManager.recreate_executor()
    function_registry[func.__name__] = func

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if os.environ.get('INSUBPROC', 'Not Set') == "True":
            raise Exception("easy_multiprocess does not allow nested subprocesses")
        
        args = list(args)
        for i, arg in enumerate(args):
            if isinstance(arg, FutureResult):
                args[i] = arg.result()

        for key, value in kwargs.items():
            if isinstance(value, FutureResult):
                kwargs[key] = value.result()

        executor = ProcessPoolManager.get_executor()
        future = executor.submit(execute_from_registry, func.__name__, *args, **kwargs)
        return FutureResult(future)
    return wrapper

concurrent = parallelize # Alias, concurrent is technically the correct term

class FutureResult:
    def __init__(self, future):
        self._future = future

    def result(self):
        r = self._future.result()
        if r not in future_result_types:
            future_result_types.append(type(r))
            wrap_magic_methods(FutureResult, type(r))
        return r

# Function to create a dynamic method
def create_dynamic_method(cls, name):
    def dynamic_method(self, *args, **kwargs):
        real_result = self.result()
        method = getattr(real_result, name)
        return method(*args, **kwargs)
    setattr(cls, name, dynamic_method)

def wrap_magic_methods(cls, typ):
    exclude = ['__class__', '__new__', '__init__', '__getattribute__', '__setattr__', '__delattr__', '__bases__', '__dict__', '__name__', '__mro__', '__slots__', '__module__']
    for name in dir(typ):
        if name.startswith('__') and name.endswith('__') and name not in exclude:
            create_dynamic_method(cls, name)

future_result_types = [int, float, str, list, dict, tuple, set, frozenset, bool, complex]
for typ in future_result_types:
    wrap_magic_methods(FutureResult, typ)