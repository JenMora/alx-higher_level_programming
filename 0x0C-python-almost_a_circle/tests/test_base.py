#!/usr/bin/python3
"""This is a module that defines unittest for base.py"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """
    This is a class for Unittests for testing
    instantiation of the Base class.
    """

    def test_no_arg(self):
        """
        This method tests if ids are consecutive when no arguments are
        passed to Base constructor.
        """

        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        """This method tests if the id is correctly assigned
        when a unique id is provided.
        """

        self.assertEqual(12, Base(12).id)

    def test_None_id(self):
        """
        This method tests if ids are consecutive when None is passed as
        an argument to Base constructor.
        """

        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        """
        This method tests if ids are consecutive when three
        Base instances are created.
        """

        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_nb_instances_after_unique_id(self):
        """This method tests if the id difference is maintained after
        creating an instance with a unique id.
        """

        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        """This methodest if the id attribute can be publicly changed."""
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        """Thi s method tests if __nb_instances attribute is
        private and inaccessible.
        """

        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)
# Additional test cases for different id types

    def test_str_id(self):
        """
        This method tests whether there is a string
        id and works correctly
        """
        self.assertEqual("hello", Base("hello").id)

    def test_bytes_id(self):
        """Test if the id attribute works correctly with bytes as input."""
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        """Test if the id attribute works correctly with
        a bytearray as input.
        """

        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        """Test if the id attribute works correctly with a
        memoryview as input.
        """

        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        """Test if the id attribute works correctly with
        positive infinity as input.
        """

        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        """
        Test if the id attribute works correctly with
        NaN (Not a Number) as input.
        """

        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        """Test if TypeError is raised when two arguments are
        passed to Base constructor.
        """

        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_float_id(self):
        """This method tests for a float id and works correctly"""
        self.assertEqual(59.5, Base(59.5).id)

    def test_complex_id(self):
        """This method tests for a complex id and works correctly"""
        self.assertEqual(complex(54), Base(complex(54)).id)

    def test_dict_id(self):
        """This method test for a dictionary id and works correctly"""
        self.assertEqual({"alpha": 5, "betty": 22}, \n
                         Base({"alpha": 5, "betty": 22}).id)

    def test_bool_id(self):
        """This method sets for a booleon id and works correctly"""
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        """This method test for a list id and works correctly"""
        self.assertEqual([2, 4, 3], Base([2, 4, 3]).id)

    def test_tuple_id(self):
        """This method checks for a tuple id and works correctly"""
        self.assertEqual((6, 5, 4), Base((6, 5, 4)).id)

    def test_set_id(self):
        """This method test for a set id and works correctly"""
        self.assertEqual({11, 12, 13}, Base({11, 12, 13}).id)

    def test_frozenset_id(self):
        """ This method tests for a frozen set id and works correctly"""
        self.assertEqual(frozenset({10, 20, 30}), \n
                         Base(frozenset({10, 20, 30})).id)

    def test_range_id(self):
        """This method tests for a range id and works correctly"""
        self.assertEqual(range(10), Base(range(10)).id)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_to_json_string_rectangle_type(self):
        """
        This method tests if the to_json_string method
        returns a JSON-formatted string for Rectangle objects.
        """

        r = Rectangle(12, 17, 20, 18, 16)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        """
        This method tests if the to_json_string method
        correctly serializes a single Rectangle dictionary.
        """

        r = Rectangle(12, 17, 20, 18, 16)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_two_dicts(self):
        """
        This is a method that test if the to_json_string method
        correctly serializes a list of two Rectangle dictionaries.
        """

        r1 = Rectangle(20, 13, 25, 19, 12)
        r2 = Rectangle(40, 27, 40, 11, 32)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)))

    def test_to_json_string_square_type(self):
        """
        This tests if the to_json_string method returns a
        JSON-formatted string for Square objects.
        """

        s = Square(10, 20, 30, 14)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        """
        This tests if the to_json_string method correctly
        serializes a single Square dictionary.
        """

        s = Square(10, 20, 30, 14)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_two_dicts(self):
        """
        This method tests if the to_json_string method correctly
        serializes a list of two Square dictionaries.
        """

        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)))

    def test_to_json_string_empty_list(self):
        """
        This tests if the to_json_string method correctly
        handles an empty list.
        """

        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        """
        Tests if the to_json_string method correctly
        handles a None argument."""
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        """
        Test if the to_json_string method raises a TypeError when
        called with no arguments.
        """

        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        """This method tests if the to_json_string method raises a
        TypeError when called with more than one argument.
        """

        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)
