import unittest
from unittest.mock import patch
from io import StringIO
from check_email import check_address

class emailTest(unittest.TestCase):

    def runTest(self, given_answers, expected_out):
        with patch('builtins.input', side_effect=given_answers), patch('sys.stdout', new=StringIO()) as fake_out:
            rv=check_address()
            self.assertEqual(fake_out.getvalue().strip(), expected_out)
            return rv
    
    def test1(self):
        a=self.runTest(["toto@yahoo.com"], "OK")
        self.assertEqual(a, "toto@yahoo.com")

    def test2(self):
        self.runTest(["quit"], "Bye!")

    def test3(self):
        self.runTest(["exit"], "Bye!")

    def test4(self):
        self.runTest(["basta"], "Bye!")

    def test5(self):
        self.runTest(["abracadabra", "quit"], "Try again\nBye!")

    def test6(self):
        a=self.runTest(["abracadabra", "toto@yahoo.com"], "Try again\nOK")
        self.assertEqual(a, "toto@yahoo.com")
    
    def test7(self):
        a=self.runTest(["abracadabra", "machintruc", "toto@yahoo.com"], "Try again\nTry again\nOK")
        self.assertEqual(a, "toto@yahoo.com")

if __name__ == "__main__":
    unittest.main()