import unittest

from monde import Monde

class mondialTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(mondialTest, self).__init__(*args, **kwargs)
        self.m=Monde()

    def test1(self):
        actual=self.m.regime("France")
        expected="republic"
        self.assertEqual(actual, expected)

    def test2(self):
        actual=self.m.regime("Albania")
        expected="emerging democracy"
        self.assertEqual(actual, expected)

    def test3(self):
        actual=self.m.regime("Austria")
        expected="federal republic"
        self.assertEqual(actual, expected)

    def test4(self):
        actual=self.m.regime("Belgium")
        expected="constitutional monarchy"
        self.assertEqual(actual, expected)

    def test5(self):
        actual=self.m.regime("Croatia")
        expected="parliamentary democracy"
        self.assertEqual(actual, expected)

    def test6(self):
        actual=self.m.regime("Spain")
        expected="parliamentary monarchy"
        self.assertEqual(actual, expected)

    def test7(self):
        actual=self.m.regime("Bahrain")
        expected="traditional monarchy"
        self.assertEqual(actual, expected)

    def test8(self):
        actual=self.m.regime("Brunei")
        expected="constitutional sultanate"
        self.assertEqual(actual, expected)
    
    def test9(self):
        actual=self.m.regime("Burma")
        expected="military regime"
        self.assertEqual(actual, expected)

    def test10(self):
        with self.assertRaises(ValueError):
            self.m.regime("Mordor")

if __name__ == "__main__":
    unittest.main()