#!/usr/bin/python3
"""
This module is the Unittest for square.
"""

import unittest
from models.base import Base
from models.square import Square
import sys
from unittest.mock import patch
import io


class TestSquare(unittest.TestCase):
    """
    This class Contains unit tests for the Square
    """

    def size_int(self):
        """
        Tests size of int type.
        """
        s1 = Square(3)
        self.assertEqual(s1.size, 3)

    def size_not_int(self):
        """
        Tests size of wrong type.
        """
        with self.assertRaises(TypeError):
            s1 = Square("3")

    def size_zero(self):
        """
        Tests zero size.
        """
        with self.assertRaises(ValueError):
            s1 = Square(0)

    def size_neg(self):
        """
        Tests negative size.
        """
        with self.assertRaises(ValueError):
            s1 = Square(-2)

    def int_x(self):
        """
        This method tests x of int type.
        """
        s1 = Square(5, 4, 7)
        self.assertEqual(s1.x, 4)

    def non_int_x(self):
        """
        Testing for non int x
        """
        with self.assertRaises(TypeError):
            s1 = Square(10, "3", 1)

    def neg_x(self):
        """
        This method tests negative x int.
        """
        with self.assertRaises(ValueError):
            s1 = Square(10, -3, 1)

    def int_y(self):
        """
        This method tests for y
        """
        s1 = Square(10, 2, 3)
        self.assertEqual(s1.y, 3)

    def non_int_y(self):
        """
        This method tests y for non int
        """
        with self.assertRaises(TypeError):
            s1 = Square(10, 3, "5")

    def neg_y(self):
        """
        This method tests negative int y.
        """
        with self.assertRaises(ValueError):
            s1 = Square(10, 3, -1)

    def area(self):
        """
        This method tests for the area of square.
        """
        s1 = Square(4)
        self.assertEqual(s1.area(), 16)
        s2 = Square(8, 0, 0, 12)
        self.assertEqual(s2.area(), 64)
        s3 = Square(10)
        self.assertEqual(s3.area(), 100)

    def display(self):
        """
        This method tests displays the square
        """
        s1 = Square(2)
        output = io.StringIO()
        with patch("sys.stdout", new=output) as capturedOutput:
            s1.display()
            capturedOutput = output.getvalue()
            stdout = "##\n##\n"
        self.assertEqual(capturedOutput, stdout)

    def str(self):
        """
        This method tests the string representation of teh square
        """
        s1 = Square(5)
        res = "[Square] (1) 0/0 - 5"
        self.assertEqual(str(s1), res)
        s2 = Square(2, 2)
        res = "[Square] (2) 2/0 - 2"
        self.assertEqual(str(s2), res)

    def tearDown(self):
        """
        This method deallocates resources.
        """
        Base._Base__nb_objects = 0

    def args(self):
        """
        This method tests for *args.
        """
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")


if __name__ == '__main__':
    unittest.main()
