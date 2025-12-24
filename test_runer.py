import unittest
from runer import check

class TestCheck(unittest.TestCase):
    def test_check(self):
        self.assertTrue(check(2))
        self.assertTrue(check(6))
        self.assertTrue(check(220))

        self.assertFalse(check(5))
        self.assertTrue(not check(7))
        self.assertTrue(not check(35))

def test_remains(self):
    self.assertEqual(remains(10, 3), 1)
    self.assertEqual(remains(20, 4), 0)


