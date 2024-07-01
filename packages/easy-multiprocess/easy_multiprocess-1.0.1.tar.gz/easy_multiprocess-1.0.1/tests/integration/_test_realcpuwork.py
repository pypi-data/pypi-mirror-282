
import time
import hashlib
import math

from easy_multiprocess import parallelize

@parallelize
def real_task(duration=0.1):
    end_time = time.time() + duration
    while time.time() < end_time:
        h = hashlib.sha256(b"some random bytes").hexdigest()
    
    return h

@parallelize
def real_task2(duration=0.1):
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        s = math.sin(i)
        i += 0.01

    return s

start_time = time.time()
h = real_task()
s = real_task2()
print(h, s)
elapsed_time = time.time() - start_time
print(f"Elapsed time: {elapsed_time} seconds")
