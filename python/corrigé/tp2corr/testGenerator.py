import unittest
from generator import fibgen

MAXITER=1000
MESSAGE_MAXITER="Too many iterations, probably an infinite loop"

class GeneratorTest(unittest.TestCase):
    def testInfiniteGenerator(self):
        i1 = 1
        i2 = 0
        passed = True
        f = fibgen()
        count_=0
        for n in f:
            count_+=1
            if count_> MAXITER:
                self.fail(MESSAGE_MAXITER)
            passed &= (n == i1+i2)
            i1 = i2
            i2 = n
            if n > 1_000_000_000_000:
                break
        self.assertTrue(passed)

    def testFiniteGenerator(self):
        expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
        count_=0
        actual=[]
        for i in fibgen(500):
            actual.append(i)
            count_+=1
            if count_> MAXITER:
                self.fail(MESSAGE_MAXITER)
        self.assertEqual(actual, expected)

if __name__=='__main__':
    unittest.main()