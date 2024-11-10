import unittest
from my_methods import get_id
import sys
import os

# Add the project root directory to the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestGetId(unittest.TestCase):
    def test_get_id(self):
        self.assertEqual(get_id(), 1)


if __name__ == '__main__':
    unittest.main()
