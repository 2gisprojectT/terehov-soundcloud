from Day1007_GetStarted.class_numbers import Numbers

__author__ = 'Alexey'

import unittest


class NumbersTest(unittest.TestCase):
    def test_init(self):
        num = Numbers(1, 2, 3)
        self.assertEqual(1, num.a, "Wrong a value")
        self.assertEqual(2, num.b, "Wrong b value")
        self.assertEqual(3, num.c, "Wrong c value")

    def test_sum(self):
        msg = "Wrong sum function"
        a = 100
        b = 200
        c = -300
        num = Numbers(a, b, c)
        self.assertEqual(num.sum(), a + b, msg)

        a = 100
        b = 200
        c = 300
        num = Numbers(a, b, c)
        self.assertEqual(num.sum(), a + b + c, msg)

    def test_multiplication(self):
        msg = "Wrong multiplication function"
        a = 0
        b = 10
        c = 1
        num = Numbers(a, b, c)
        self.assertEqual(num.multiplication(), a * b * c, msg)

        a = 1.5
        b = 2
        c = 1.33
        num = Numbers(a, b, c)
        self.assertEqual(num.multiplication(), a * b * c, msg)

        a = 0
        b = 10
        c = -20
        num = Numbers(a, b, c)
        self.assertEqual(num.multiplication(), a * b * c, msg)

    def test_abs_multiplication(self):
        msg = "Wrong abs multiplication"
        a = -1
        b = 10
        c = 10
        num = Numbers(a, b, c)
        self.assertEqual(num.abs_multiplication(), -a * b * c, msg)

        a = -1
        b = 0
        c = 10
        num = Numbers(a, b, c)
        self.assertEqual(num.abs_multiplication(), 0, msg)


if __name__ == '__main__':
    unittest.main()
