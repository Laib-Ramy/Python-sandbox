import unittest
from types import LambdaType
from lambdas import *

def isLambda(f):
    return type(f) is LambdaType and f.__code__.co_name=='<lambda>'

class lambdassTest(unittest.TestCase):
    def test1(self):
        self.assertTrue(isLambda(is_multiple_of(3)))

    def test2(self):
        self.assertEqual(list(filter(is_multiple_of(4), range(20))),
                         [0, 4, 8, 12, 16])
        self.assertEqual(list(filter(is_multiple_of(3), range(20))),
                         [0, 3, 6, 9, 12, 15, 18])

    def test3(self):
        f=binary('+')
        for a in range(-10, 10): 
            for b in range(-10,10):
                self.assertEqual(f(a,b), a+b)

    def test4(self):
        f=binary('-')
        for a in range(-10, 10): 
            for b in range(-10,10):
                self.assertEqual(f(a,b), a-b)

    
    def test5(self):
        f=binary('*')
        for a in range(-10, 10): 
            for b in range(-10,10):
                self.assertEqual(f(a,b), a*b)

    def test6(self):
        f=binary('==')
        for a in range(-10, 10): 
            for b in range(-10,10):
                self.assertEqual(f(a,b), a==b)


if __name__ == "__main__":
    unittest.main()
