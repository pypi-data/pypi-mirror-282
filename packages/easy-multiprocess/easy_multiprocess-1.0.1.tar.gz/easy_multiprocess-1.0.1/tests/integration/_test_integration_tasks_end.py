
import time

from easy_multiprocess import ProcessPoolManager

executor = ProcessPoolManager.get_executor()

def delayed_func():
    time.sleep(0.1)
    print("PRINT OUTPUT AFTER 0.1 SECOND")

executor.submit(delayed_func)