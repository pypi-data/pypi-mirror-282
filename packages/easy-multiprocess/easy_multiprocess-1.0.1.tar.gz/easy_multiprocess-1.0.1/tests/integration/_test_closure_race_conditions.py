
import time
import hashlib
import math
from concurrent.futures import ProcessPoolExecutor

from easy_multiprocess import parallelize



with ProcessPoolExecutor() as executor:
    x = 5
    def func1(num):
        return x

    fut1 = executor.submit(func1, x)
    x = 7
    fut2 = executor.submit(func1, x)
    print(fut1.result())
    print(fut2.result())