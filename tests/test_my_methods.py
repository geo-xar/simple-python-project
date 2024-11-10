import unittest
from my_module.my_methods import get_id


class TestGetId(unittest.TestCase):
    def test_get_id(self):
        self.assertEqual(get_id(), 1)


if __name__ == '__main__':
    unittest.main()
