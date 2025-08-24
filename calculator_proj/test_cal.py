import unittest
from calc import add, sub

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)

    def test_sub(self):
        self.assertEqual(sub(5,2),3)

if __name__ == "__main__":
    unittest.main()
