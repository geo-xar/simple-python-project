import unittest
import sys
import os

# Add the project root directory to the PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from my_module.my_methods import get_id


class TestGetId(unittest.TestCase):
    def test_get_id(self):
        self.assertEqual(get_id(), 1)


if __name__ == '__main__':
    unittest.main()
