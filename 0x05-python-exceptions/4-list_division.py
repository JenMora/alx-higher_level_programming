#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    alist = []
    for i in range(0, list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong input, try again")
            division = 0
        except ZeroDivisionError:
            print("division by 0 is infinite")
            division = 0
        except IndexError:
            print("The output is out of range")
            division = 0
        finally:
            alist.append(division)
    return alist
