#!/usr/bin/python3
class MyList(list):
    """
    This is a class Mylist that inherist from the class list
    """
    def print_sorted(self):
        """
        This is a public method that prints a sorted list and
        inherits from the ("class List")
        Arguments:
        list
        Returns:
        nothing
        """

        sorted_list = sorted(self)
        print(sorted_list)
