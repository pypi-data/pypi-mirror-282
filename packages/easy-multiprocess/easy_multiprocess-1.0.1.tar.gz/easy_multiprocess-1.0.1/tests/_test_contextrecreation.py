
from easy_multiprocess import parallelize, ProcessPoolManager

import time


@parallelize
def fun(y=None):
    if y:
        return y
    time.sleep(1)
    return x

fun() # First submission to processpoolexecutor fixes context

x = 7

print(fun()) # prints 5

ProcessPoolManager.recreate_executor() # Recreate executor

print(fun()) # prints 7