import unittest
from point import Point
import point

class SpecialMethodsTest(unittest.TestCase):
    def testConstructor(self):
        p = Point(2, 3)
        self.assertEqual((p.x, p.y), (2, 3))

    def testEquality(self):
        p1 = Point(2, 3)
        p2 = Point(2, 3)
        self.assertEqual(p1, p2)

    def testInequality(self):
        p1 = Point(1, 2)
        p2 = Point(2, 3)
        self.assertNotEqual(p1, p2)

    def testHash(self):
        p1 = Point(2, 3)
        p2 = Point(2, 3)
        self.assertEqual(hash(p1), hash(p2))

    def testStr(self):
        p = Point(4, 5)
        self.assertEqual(str(p), '(4, 5)')

    def testRepr(self):
        p = Point(5, 6)
        self.assertEqual(repr(p), 'point.Point(5, 6)')

    def testEval(self):
        p1 = Point(7, 8)
        p2 = eval(repr(p1))
        self.assertEqual(p1, p2)

if __name__=='__main__':
    unittest.main()