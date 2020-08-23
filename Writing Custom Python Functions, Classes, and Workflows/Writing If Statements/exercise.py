"""
Writing If Statements
Author: Leon Shpaner
Date:   August 9, 2020
"""

def find_min(a,b):
    """
    Returns the lesser of two inputs a and b
    """
    if a<b:
        return a
    else:
        return b


def test_for_equality(a,b):
    """
    Returns True if a and b are equal, or False otherwise
    """
    if a==b:
        return True
    else:
        return False


def test_for_3or4(a):
    """
    Returns the string "input is equal to 3" if the input a is equal to 3,
    "input is equal to 4" if a is equal to 4, and
    "input is not equal to 3 or 4" if neither case is true
    """

    if a==3:
        return "input is equal to 3"
    elif a==4:
        return "input is equal to 4"
    else:
        return "input is not equal to 3 or 4"
    