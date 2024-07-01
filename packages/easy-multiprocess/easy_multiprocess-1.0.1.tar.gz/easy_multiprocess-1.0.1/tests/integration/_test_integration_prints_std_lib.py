
from concurrent.futures import ProcessPoolExecutor
import time

executor = ProcessPoolExecutor()

def delayed_func():
    time.sleep(0.1)
    print("PRINT OUTPUT AFTER 0.1 SECOND")

r = executor.submit(delayed_func)

# Concurrent futures will only print one time
r.result()
r.result()

