#!/usr/bin/python3
"""
This module contains the Unittest for  the rectangle
"""
import sys
from unittest.mock import patch
import io
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Contains unit tests for the Rectangle Class.
    """

    def width_int(self):
        """
        This method tests rectangle width of int type.
        """
        r1 = Rectangle(12, 4)
        self.assertEqual(r1.width, 12)

    def width_not_int(self):
        """
        This method tests width of wrong type.
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle("trs", 34)

    def width_zero(self):
        """
        This method tests for zero rectangle width.
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)

    def width_neg(self):
        """
        This method tests negative rectangle width.
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, 2)

    def height_int(self):
        """
        This method tests height of int type.
        """
        r1 = Rectangle(18, 9)
        self.assertEqual(r1.height, 9)

    def height_not_int(self):
        """
        This method tests height of wrong type.
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, "tsr")

    def height_zero(self):
        """
        This method tests zero height.
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 0)

    def test_height_neg(self):
        """
        This method tests negative rectangle height.
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -8)

    def x_int(self):
        """
        This method tests x of int type.
        """
        r1 = Rectangle(10, 7, 3, 91)
        self.assertEqual(r1.x, 3)

    def x_not_int(self):
        """
        This method tests x of wrong type.
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, "yts", 1)

    def test_x_neg(self):
        """
        This method tests for negative x.
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(11, 20, -5, 1)

    def test_y_int(self):
        """
        This method tests y of int type.
        """
        r1 = Rectangle(10, 2, 3, 1)
        self.assertEqual(r1.y, 1)

    def test_y_not_int(self):
        """
        This method tests y of wrong type.
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, 3, "1")

    def test_y_neg(self):
        """
        This method tests for negative y.
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2, 3, -7)

    def test_area(self):
        """
        This method tests area of rectangle.
        """
        r1 = Rectangle(20, 40)
        self.assertEqual(r1.area(), 800)
        r2 = Rectangle(8, 4, 0, 0, 12)
        self.assertEqual(r2.area(), 32)
        r3 = Rectangle(10, 20)
        self.assertEqual(r3.area(), 200)

    def str(self):
        """
        This method tests for str representation
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        res = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r1), res)
        r2 = Rectangle(5, 5, 1)
        res = "[Rectangle] (1) 1/0 - 5/5"
        self.assertEqual(str(r2), res)

    def args(self):
        """
        This method tests for *args.
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

    def tearDown(self):
        """
        Deallocating resources.
        """
        Base._Base__nb_objects = 0


if __name__ == '__main__':
    unittest.main()
