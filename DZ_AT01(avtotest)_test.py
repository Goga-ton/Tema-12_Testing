import unittest
from DZ_AT01_avtotest_cod import remains

class TestMath(unittest.TestCase):
    def test_remains1(self):
        self.assertEqual(remains(100, 7), 2)
    def test_remains2(self):
        self.assertRaises(ValueError, remains, 5, 0)
    def test_remains3(self):
        self.assertNotEqual(remains(11, 4), 4)
