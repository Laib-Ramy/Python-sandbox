import unittest
from decorators import insist, keep_calm

@keep_calm
def may_fail(do_fail):
    if do_fail:
        raise Exception
    return 42

@insist
def programmed_failure(n_failures, counter):
    counter[0]+=1
    if counter[0]>n_failures:
        return counter[0]
    raise Exception


class decoratorsTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(may_fail(False), 42)

    def test2(self):
        self.assertEqual(may_fail(True), None)

    def test3(self):
        self.assertEqual(programmed_failure(1,[0]), 2)

    def test4(self):
        self.assertEqual(programmed_failure(10,[0]), 11)

    def test5(self):
        self.assertEqual(programmed_failure(100,[0]), 101)

if __name__ == "__main__":
    unittest.main()