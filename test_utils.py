import unittest
from utils import double

class TestUtils(unittest.TestCase):
    def test_double(self):
        self.assertEqual(double(2), 4)
        self.assertEqual(double(3), 6)
        self.assertEqual(double(0), 0)

if __name__ == '__main__':
    unittest.main()
