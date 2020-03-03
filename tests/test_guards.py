import os
import unittest

import sys; sys.path.append("..")
from pyimport.main import path_guard, init_guard


class TestGuards(unittest.TestCase):
    def test_path_guard(self) -> None:
        target_path = ".."
        path_guard("..")
        self.assertTrue(target_path in sys.path)

    def test_init_guard(self) -> None:
        own_path = os.path.abspath(__file__)
        init = init_guard(own_path)
        self.assertTrue(init.IMPORTED)

if __name__ == "__main__":
    unittest.main()
