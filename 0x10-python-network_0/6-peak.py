#!/usr/bin/python3
"""
This module contains a function called find_peak that searches for a peak
in a list of unsorted integers.
"""

def find_peak(numbers):
    """
    This method finds a peak in a list of unsorted integers.
    """
    if numbers is None or len(numbers) == 0:
        return None
    left = 0
    right = len(numbers)

    while left < right:
        middle = (left + right) // 2
        if (middle == 0 or numbers[middle] >= numbers[middle - 1]) \
                and (middle == right - 1 or
                     numbers[middle] >= numbers[middle + 1]):
            return numbers[middle]
        elif middle > 0 and numbers[middle] < numbers[middle - 1]:
            right = middle
        else:
            left = middle + 1
    return None
