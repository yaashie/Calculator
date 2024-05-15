import unittest
from calculator import Calculate


class TestMath(unittest.TestCase):
    def test_add(self):
        answer = Calculate.add(2, 4)
        self.assertEqual(answer, 6)

    def test_sub(self):
        answer = Calculate.sub(4,2)
        self.assertEqual(answer, 2)

    def test_sub_negative(self):
        answer = Calculate.sub(2,4)
        self.assertEqual(answer, -2)

    def test_multiply(self):
        answer = Calculate.multiply(2,3)
        self.assertEqual(answer, 6)

    def test_divide(self):
        answer = Calculate.divide(4,2)
        self.assertEqual(answer, 2)

    def test_divide_zero(self):
        with self.assertRaises(ZeroDivisionError):
            Calculate.divide(4,0)


if __name__ == '__main__':
    unittest.main()