import unittest
import inspect
from arguments import *


class argumentsTest(unittest.TestCase):
    def test_f1_signature(self):
        par = inspect.signature(f1).parameters
        actual = [str(par[p].kind) for p in par]
        expected = ['POSITIONAL_ONLY',
                    'POSITIONAL_ONLY', 'POSITIONAL_OR_KEYWORD']
        self.assertEqual(actual, expected)

    def test_f1_name_positional_or_keyword(self):
        par = inspect.signature(f1).parameters
        self.assertTrue(str(par['arg'].kind) == 'POSITIONAL_OR_KEYWORD')

    def test_f1_returns_nothing(self):
        self.assertTrue(f1(1, 2, 3) is None)

    def test_f2_signature(self):
        par = inspect.signature(f2).parameters
        actual = [str(par[p].kind) for p in par]
        expected = ['POSITIONAL_ONLY', 'POSITIONAL_ONLY',
                    'POSITIONAL_ONLY', 'POSITIONAL_ONLY']
        self.assertEqual(actual, expected)

    def test_f2_defaults(self):
        vals = inspect.signature(f2).parameters.values()
        actual = [v.default for v in vals]
        expected = [inspect._empty, inspect._empty, 42, 5]
        self.assertEqual(actual, expected)

    def test_f2_returns_nothing(self):
        self.assertTrue(f2(1, 2) is None)

    def test_f3_signature_and_names(self):
        par = inspect.signature(f3).parameters
        actual = [str(par[p].kind) for p in ['a1', 'a2', 'a3', 'a4']]
        expected = ['POSITIONAL_OR_KEYWORD', 'POSITIONAL_OR_KEYWORD',
                    'KEYWORD_ONLY', 'KEYWORD_ONLY']
        self.assertEqual(actual, expected)

    def test_f3_returns_nothing(self):
        self.assertTrue(f3(1, 2, a3=3, a4=4) is None)

    def test_f4_signature(self):
        par = inspect.signature(f4).parameters
        actual = [str(par[p].kind) for p in par]
        expected = ['POSITIONAL_ONLY', 'POSITIONAL_ONLY', 'POSITIONAL_OR_KEYWORD',
                    'POSITIONAL_OR_KEYWORD', 'KEYWORD_ONLY', 'KEYWORD_ONLY']
        self.assertEqual(actual, expected)

    def test_f4_signature_and_names(self):
        par = inspect.signature(f4).parameters
        actual = [str(par[p].kind) for p in ['a1', 'a2', 'a3', 'a4']]
        expected = ['POSITIONAL_OR_KEYWORD', 'POSITIONAL_OR_KEYWORD',
                    'KEYWORD_ONLY', 'KEYWORD_ONLY']
        self.assertEqual(actual, expected)

    def test_f4_returns_nothing(self):
        self.assertTrue(f4(0, 0, 1, 2, a3=3, a4=4) is None)

    def test_f5_signature(self):
        par=inspect.signature(f5).parameters
        actual = [str(par[p].kind) for p in par]
        expected=['POSITIONAL_ONLY', 'POSITIONAL_ONLY', 'VAR_POSITIONAL']
        self.assertEqual(actual, expected)

    def test_f5_return(self):
        self.assertEqual(f5(1,2), [1,2])
        self.assertEqual(f5(1,2,3), [1,2,3])
        self.assertEqual(f5(1,2,3,4), [1,2,3,4])
        self.assertEqual(f5(1,2,3,4,5), [1,2,3,4,5])

    def test_f6_signature(self):
        par=inspect.signature(f6).parameters
        actual = [str(par[p].kind) for p in par]
        expected=['KEYWORD_ONLY', 'KEYWORD_ONLY', 'VAR_KEYWORD']
        self.assertEqual(actual, expected) 

    def test_f6_defaults(self):
        vals=inspect.signature(f6).parameters.values()
        actual=[v.default for v in vals]
        expected=[5, 6, inspect._empty]
        self.assertEqual(actual, expected) 

    def test_f6_return(self):
        self.assertEqual(f6(), {'a1': 5, 'a2': 6})
        self.assertEqual(f6(x=7), {'a1': 5, 'a2': 6, 'x':7})
        self.assertEqual(f6(x=7, y=8), {'a1': 5, 'a2': 6, 'x':7, 'y':8})

    def test_f7_signature(self):
        par=inspect.signature(f7).parameters
        actual = [str(par[p].kind) for p in par]
        expected=['VAR_POSITIONAL', 'VAR_KEYWORD']
        self.assertEqual(actual, expected) 

    def test_f7_return(self):
       self.assertEqual(f7(), (0,0)) 
       self.assertEqual(f7(1), (1,0)) 
       self.assertEqual(f7(1,2), (2,0)) 
       self.assertEqual(f7(1,2, a=3), (2,1))
       self.assertEqual(f7(1,2, a=3, b=4), (2,2))


if __name__ == "__main__":
    unittest.main()
