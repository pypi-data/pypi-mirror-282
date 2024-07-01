
import time

from easy_multiprocess import ProcessPoolManager, FutureResult

# Make a decorator around the ProcessPoolManager.shutdown method, which will print a message when it is called, which we can then check for in the test
def shutdown_decorator(func):
    def wrapper(*args, **kwargs):
        print(f)
        print("Time taken: ", time.time() - s)
        return func(*args, **kwargs)
    
    return wrapper

ProcessPoolManager.cleanup = shutdown_decorator(ProcessPoolManager.cleanup)

# ProcessPoolManager.shutdown()

def delayed_func(x):
    time.sleep(x)
    # print("Slept for {} seconds".format(x))
    return x*x

s = time.time()
r = ProcessPoolManager.get_executor().submit(delayed_func, 0.1)
f = FutureResult(r)
