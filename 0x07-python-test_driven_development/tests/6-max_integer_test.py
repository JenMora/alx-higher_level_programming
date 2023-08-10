#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        ret = max_integer([100, 2, 30, 10])
        self.assertEqual(ret, 100)
        ret = max_integer([105, 103, 405, 320])
        self.assertEqual(ret, 405)
        ret = max_integer([1, 0, -12, -0])
        self.assertEqual(ret, 1)

    def test_single_element(self):
        ret = max_integer([8])
        self.assertEqual(ret, 8)

    def test_empty_list(self):
        ret = max_integer([])
        self.assertIsNone(ret)

    def test_zero(self):
        ret = max_integer([0, 0, 0])
        self.assertEqual(ret, 0)

    def test_large_numbers(self):
        ret = max_integer([1230, 455670, 43123, 9870, 1034])
        self.assertEqual(ret, 455670)

    def test_negative_num(self):
        ret = max_integer([-1, -123, -5, -10])
        self.assertEqual(ret, -1)

    def test_negative_with_zero(self):
        ret = max_integer([-1, -34, 0, -976, -3])
        self.assertEqual(ret, 0)

if __name__ == '__main__':
    unittest.main()
