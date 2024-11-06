import unittest
from iterable import Fib

MAXITER=1000
MESSAGE_MAXITER="Too many iterations, probably an infinite loop"

class IterableTest(unittest.TestCase):
    def testFinite(self):
        expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        actual = [] 
        count_=0
        for i in Fib(10):
            actual.append(i)
            count_+=1
            if count_> MAXITER:
                self.fail(MESSAGE_MAXITER)
        self.assertEqual(actual, expected)

    def testContains(self):
        self.assertTrue(280571172992510140037611932413038677189525 in Fib())

    def testDoesNotContain(self):
        self.assertFalse(280571172992510140037611932413038677189526 in Fib())

if __name__=='__main__':
    unittest.main()