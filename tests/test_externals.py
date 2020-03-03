import os
import unittest

import sys; sys.path.append("..")
from pyimport.main import get_resource


class TestExternals(unittest.TestCase):
    def test_get_resource(self) -> None:
        resource_path = os.path.abspath("non-package/external/external_resource.py")
        resource = get_resource(resource_path)
        self.assertTrue(resource.IMPORTED)


if __name__ == "__main__":
    unittest.main()
