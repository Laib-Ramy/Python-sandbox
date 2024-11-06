import unittest

from telephone import internationalize

class telephoneTest(unittest.TestCase):
    def test1(self):
        actual=internationalize('01-69-15-69-39')
        expected='+33-1-69-15-69-39'
        self.assertEqual(actual, expected)

    def test2(self):
        actual=internationalize('06-12-34-56-78')
        expected='+33-6-12-34-56-78'
        self.assertEqual(actual, expected)

    def test3(self):
        with self.assertRaises(ValueError):
            internationalize('12-34-56-78-90')

    def test4(self):
        with self.assertRaises(ValueError):
            internationalize('0123456789')

if __name__ == "__main__":
    unittest.main()