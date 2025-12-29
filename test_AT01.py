import unittest
from AT01_avtotesting_v1 import add, subtract, multiply, divide, dividenull


class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 2), 7)
        self.assertNotEqual(add(11, 4), 4)
    def test_subtract(self):
        self.assertEqual(subtract(11, 5), 6)
        self.assertNotEqual(subtract(18, 2), 11)
    def test_multiply(self):
        self.assertEqual(multiply(5, 5), 25)
        self.assertNotEqual(multiply(18, 2), 30)
    def test_divide(self):
        self.assertEqual(divide(12, 3), 4)
        self.assertNotEqual(divide(18, 2), 10)
    def test_div_not_null(self):
        self.assertEqual(divide(18, 2), 9)
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(35, 7), 5)
    def test_div_null(self):
        self.assertRaises(ValueError, dividenull, 6, 0)


# так и не разобрался зачем этот код кроме как для запуска в терминале (без этого блока не запуститься)
# в целом судя по описанию от perplexity этот блок проверяет запущен ли файл на прямую и за тем выполняется
if __name__ == '__main__':
    unittest.main()



