#!/usr/bin/python3
"""
This is a Unittest module for base ckass
"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import json
import os


class TestBase(unittest.TestCase):
    """
    This class contains unit tests for the Base
    """

    def test_base_id(self):
        """
        This method is for testing any kind of id
        """
        obj1 = Base()
        self.assertEqual(obj1.id, 1)
        obj2 = Base()
        self.assertEqual(obj2.id, 2)
        obj3 = Base()
        self.assertEqual(obj3.id, 3)
        obj4 = Base(12)
        self.assertEqual(obj4.id, 12)
        obj5 = Base()
        self.assertEqual(obj5.id, 4)

    def test_to_json_string(self):
        """
        This method tests to_json_string
        """
        obj = Rectangle(7, 8, 10, 9)
        self.assertEqual(type(obj), Rectangle)
        dictionary = obj.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        json_dictionary_1 = Base.to_json_string([])
        json_dictionary_2 = Base.to_json_string(None)
        self.assertEqual(type(json_dictionary), str)
        from_json = json.loads(json_dictionary)
        self.assertEqual(json_dictionary_1, "[]")
        self.assertEqual(json_dictionary_2, "[]")
        self.assertDictEqual(from_json[0], dictionary)
        obj1 = Square(4, 8, 2)
        self.assertEqual(type(obj1), Square)
        dict_sq = obj1.to_dictionary()
        json_dict_sq = Base.to_json_string([dict_sq])
        json_dict_sq_1 = Base.to_json_string([])
        json_dict_sq_2 = Base.to_json_string(None)
        self.assertEqual(type(json_dict_sq), str)
        from_json = json.loads(json_dict_sq)
        self.assertEqual(json_dict_sq_1, "[]")
        self.assertEqual(json_dict_sq_2, "[]")
        self.assertDictEqual(from_json[0], dict_sq)

    def test_base_id(self):
        """
        This method is for testing any kind of id
        """
        obj1 = Base()
        self.assertEqual(obj1.id, 1)
        obj2 = Base()
        self.assertEqual(obj2.id, 2)
        obj3 = Base()
        self.assertEqual(obj3.id, 3)
        obj4 = Base(12)
        self.assertEqual(obj4.id, 12)
        obj5 = Base()
        self.assertEqual(obj5.id, 4)

    def test_load_from_file(self):
        """
        This method tests load_from_file
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rect_input = [r1, r2]
        Rectangle.save_to_file(list_rect_input)
        list_rect_output = Rectangle.load_from_file()
        for i in range(2):
            self.assertEqual(str(list_rect_input[i]), str(list_rect_output[i]))
            self.assertNotEqual(list_rect_input[i], list_rect_output[i])
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_sq_input = [s1, s2]
        Square.save_to_file(list_sq_input)
        list_sq_output = Square.load_from_file()
        for i in range(2):
            self.assertEqual(str(list_sq_input[i]), str(list_sq_output[i]))
            self.assertNotEqual(list_sq_input[i], list_sq_output[i])

    def test_from_json_string(self):
        """
        This method tests from_json_string
        """
        list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
                ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)
        self.assertEqual(list_output, list_input)
        json_list_input = Rectangle.to_json_string([])
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [])

    def test_create(self):
        """
        This method tests creation of the
        """
        r1 = Rectangle(5, 7, 3)
        self.assertEqual(type(r1), Rectangle)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual((r1 is r2), False)
        self.assertEqual((r1 == r2), False)
        s1 = Square(4, 2, 4)
        self.assertEqual(type(s1), Square)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual((s1 is s2), False)
        self.assertEqual((s1 == s2), False)

    def tearDown(self):
        """
        Deallocating resources.
        """
        Base._Base__nb_objects = 0
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        try:
            os.remove("Square.json")
        except Exception:
            pass


if __name__ == '__main__':
    unittest.main()
