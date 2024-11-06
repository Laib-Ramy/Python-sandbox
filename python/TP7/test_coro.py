import unittest
import random
from coro import *

class coroTest(unittest.TestCase):
    def test1(self):
        ra=running_average()
        acc=0.
        for n in range(1,10):
            x=random.random()
            acc+=x
            av=acc/n
            self.assertAlmostEqual(av, ra.send(x), places=10)

if __name__ == "__main__":
    unittest.main()