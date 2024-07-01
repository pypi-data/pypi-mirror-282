
import time

from easy_multiprocess import parallelize, ProcessPoolManager

ProcessPoolManager.set_max_workers(5)

sleep_time = 0.1

class TestDelayed:
    @parallelize
    def delayed_func_class(self):
        time.sleep(sleep_time)
        print("PRINT OUTPUT AFTER {sleep_time} SECOND")
        return 5

s = time.time()
t = TestDelayed()
r2 = [t.delayed_func_class() for i in range(4)]
print(r2)
e = time.time()
print(f"Time taken 1: ", e - s)

@parallelize
def delayed_func():
    time.sleep(sleep_time)
    print("Simple case: wait {sleep_time} second")
    return 3
    
s = time.time()
r = [delayed_func() for _ in range(4)]
assert r == [3, 3, 3, 3]
e = time.time()
print(f"Time taken 2: ", e - s)

def delayed_func_outer():
    @parallelize
    def delayed_func_inner():
        time.sleep(sleep_time)
        print("Inner case sleep {sleep_time} second")
        return 2
    
    return [delayed_func_inner() for _ in range(2)]
    
s = time.time()
r = delayed_func_outer()
assert r == [2, 2]
e = time.time()
print(f"Time taken 3: ", e - s)
