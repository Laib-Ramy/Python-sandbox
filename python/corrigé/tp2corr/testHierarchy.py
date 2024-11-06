import unittest
from hierarchy import *

class HierarchyTest(unittest.TestCase):
    def testPrototheriaIsMammalia(self):
        self.assertEqual((Mammalia,), Prototheria.__bases__)

    def testMonotremataIsPrototheria(self):
        self.assertEqual((Prototheria,), Monotremata.__bases__)

    def testTheriaIsMammalia(self):
        self.assertEqual((Mammalia,), Theria.__bases__)

    def testEutheriaIsTheria(self):
        self.assertEqual((Theria,), Eutheria.__bases__)

    def testPlacentaliaIsEutheria(self):
        self.assertEqual((Eutheria,), Placentalia.__bases__)

    def testXenarthraIsPlacentalia(self):
        self.assertEqual((Placentalia,), Xenarthra.__bases__)

    def testAfrotheriaIsPlacentalia(self):
        self.assertEqual((Placentalia,), Afrotheria.__bases__)

    def testBoreoeutheriaIsPlacentalia(self):
        self.assertEqual((Placentalia,), Boreoeutheria.__bases__)

    def testMetatheriaIsTheria(self):
        self.assertEqual((Theria,), Metatheria.__bases__)

    def testMarsupialiaIsMetatheria(self):
        self.assertEqual((Metatheria,), Marsupialia.__bases__)

if __name__=='__main__':
    unittest.main()