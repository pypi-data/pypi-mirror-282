
import time
import unittest
import subprocess
from concurrent.futures import ProcessPoolExecutor

from easy_multiprocess import FutureResult

# getnum at module level so that it can be pickled by the ProcessPoolExecutor
num = 5
def getnum():
    time.sleep(0.1)
    return num

def delayed_func():
    time.sleep(0.1)
    print("PRINT OUTPUT AFTER 0.1 SECOND")

class TestProcessPoolManager(unittest.TestCase):
    def test_process_pool_manager_shutdown(self):
        output = subprocess.check_output(['python', 'tests/integration/_test_integration_shutdown.py'])
        self.assertIn(b"Time taken:  0.1", output)
        self.assertIn(b"0.01", output)
    
    def test_FutureResult_primitive(self):
        with ProcessPoolExecutor() as executor:
            A = executor.submit(getnum)
            A = FutureResult(A)
            assert A == 5
            assert A + 5 == 10
            assert 5 == A
            assert A.result() == 5
    
    def test_FutureResult_None(self):
        with ProcessPoolExecutor() as executor:
            A = executor.submit(delayed_func)
            A = FutureResult(A)
            # assert A is None # Unfortunately A is a FutureResult object - cannot fake identity
            assert A == None
            assert A != 5
            assert A is not 5

    def test_tasks_end(self):
        output = subprocess.check_output(['python', 'tests/integration/_test_integration_tasks_end.py'])
        self.assertEqual(output, b'PRINT OUTPUT AFTER 0.1 SECOND\n')
    
    def test_prints_std_lib(self):
        output = subprocess.check_output(['python', 'tests/integration/_test_integration_prints_std_lib.py'])
        self.assertEqual(output, b'PRINT OUTPUT AFTER 0.1 SECOND\n')
    
    def test_prints_easy_multiprocess(self):
        output = subprocess.check_output(['python', 'tests/integration/_test_integration_prints_easy_multiprocess.py'])
        self.assertEqual(output, b'PRINT OUTPUT AFTER 0.1 SECOND\n')
        
    def test_decorator(self):
        output = subprocess.check_output(['python', 'tests/integration/_test_decorator.py'])
        self.assertIn(b"Time taken 1:  0.1", output)
        self.assertIn(b"Time taken 2:  0.1", output)
        self.assertIn(b"Time taken 3:  0.1", output)
    
    def test_futureresult_args(self):
        output = subprocess.check_output(['python', 'tests/integration/_test_futureresult_args.py'])
        self.assertIn(b"Time taken:  0.2", output)
        self.assertIn(b"(5, 2)", output)
    
    def test_boolean(self):
        output = subprocess.check_output(['python', 'tests/integration/_test_boolean_no_delay.py'])
        self.assertIn(b"False", output)
        self.assertIn(b"True", output)
    
    def test_realcpuwork(self):
        output = subprocess.check_output(['python', 'tests/integration/_test_realcpuwork.py'])
        self.assertIn(b"Elapsed time: 0.1", output)