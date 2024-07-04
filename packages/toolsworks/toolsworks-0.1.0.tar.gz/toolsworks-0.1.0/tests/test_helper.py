import unittest
from toolsworks.helper import add

class TestHelper(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)

if __name__ == "__main__":
    unittest.main()

