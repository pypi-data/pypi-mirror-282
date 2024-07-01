
import time

from easy_multiprocess import parallelize

@parallelize
def no_delay_func():
    return False

r = no_delay_func()
if not r: # Should call __bool__
    print(r)

# Test re-assignment of variable, extraneous sanity test
r = True
if r:
    print(r)