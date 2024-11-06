import unittest
from comprehensions import *

class ComprehensionsTest(unittest.TestCase):

    def testList(self):
        expected = [7, 22, 11, 34, 17, 52, 26,
                    13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        actual = collatz_list(7)
        self.assertEqual(actual, expected)

    def testSet(self):
        expected = {1, 2, 4, 5, 7, 8, 10, 11,
                    13, 16, 17, 20, 22, 26, 34, 40, 52}
        actual = collatz_set(7)
        self.assertEqual(actual, expected)

    def testDict(self):
        expected = {1: [1],
                    2: [2, 1],
                    3: [3, 10, 5, 16, 8, 4, 2, 1],
                    4: [4, 2, 1],
                    5: [5, 16, 8, 4, 2, 1],
                    6: [6, 3, 10, 5, 16, 8, 4, 2, 1],
                    7: [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]}
        actual = collatz_dict(7)
        self.assertEqual(actual, expected)

    def testCount(self):
        expected = [1, 2, 8, 3, 6, 9, 17, 4, 20, 7]
        actual = [collatz_count(i) for i in range(1, 11)]
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()