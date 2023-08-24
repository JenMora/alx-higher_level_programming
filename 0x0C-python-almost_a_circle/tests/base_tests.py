#!/usr/bin/python3

"""testcases for base.py"""


import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """
        def test_id_increment(self):
        # Test if the id is incremented correctly for each new instance
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)
    """
    def test_custom_id(self):
        # Test if custom id assignment works
        custom_id = 42
        obj = Base(custom_id)
        self.assertEqual(obj.id, custom_id)

    def test_default_id(self):
        # Test if default id assignment works for multiple instances
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)

    def test_mixed_id_assignment(self):
        # Test if mixed custom and default id assignment works
        obj1 = Base()
        custom_id = 100
        obj2 = Base(custom_id)
        obj3 = Base()
        self.assertEqual(obj1.id, 7)
        self.assertEqual(obj2.id, custom_id)
        self.assertEqual(obj3.id, 8)

    def test_negative_custom_id(self):
        # Test if negative custom id is handled correctly
        custom_id = -1
        obj = Base(custom_id)
        self.assertEqual(obj.id, custom_id)

    def test_zero_custom_id(self):
        # Test if zero custom id is handled correctly
        custom_id = 0
        obj = Base(custom_id)
        self.assertEqual(obj.id, custom_id)

    def test_instance_count(self):
        # Test if the number of objects created is tracked accurately
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(Base._Base__nb_objects, 6)

if __name__ == '__main__':
    unittest.main()
