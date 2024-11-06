import unittest

from gigasecond import add_gigasecond

class gigasecondTest(unittest.TestCase):
    def test1(self):
        actual=add_gigasecond('2021-10-18 08:30:00')
        expected='2053-06-26 10:16:40'
        self.assertEqual(actual, expected)

    def test2(self):
        actual=add_gigasecond('2021-01-01 00:00:00')
        expected='2052-09-09 01:46:40'
        self.assertEqual(actual, expected)
    
    def test3(self):
        with self.assertRaises(ValueError):
            add_gigasecond('2021-01-01 24:00:00')

    def test4(self):
        with self.assertRaises(ValueError):
            add_gigasecond('2021-01-01 23:59:60')

if __name__ == "__main__":
    unittest.main()