
import time

from easy_multiprocess import parallelize

sleep_time = 0.1

@parallelize
def delayed_func():
    time.sleep(sleep_time)
    return 2

@parallelize
def func2(val, val2=3):
    time.sleep(sleep_time)
    return val, val2

s = time.time()
r = delayed_func()
r2 = delayed_func()

f = func2(r, val2=10)
f2 = func2(5, val2=r2)
print(f)
e = time.time()
print(f"Time taken: ", e - s)
print(f2)