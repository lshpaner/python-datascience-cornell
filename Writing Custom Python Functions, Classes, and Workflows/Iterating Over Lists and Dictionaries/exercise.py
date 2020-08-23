"""
Iterating Over Lists and Dictionaries
Author: Leon Shpaner
Date:   August 9, 2020
"""

import random

my_list = [1,3,5,7,9]

my_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9}

def multiply_list_by(alist, multiplier):
    """
    Returns a new list that multiplies each element of alist by the multiplier, 
    so that the new list is the same length as alist, and the n'th element of 
    new_list is equal to multiplier times the n'th element of alist
    """
    new_list = []
    for elem in alist:
        new_list.append(elem*multiplier)
    return new_list

def print_keys_and_values(adict):
    """
    Returns a list of strings, where each key and value is converted to a 
    string, and each key-value pair is concatenated.
    NOTE: we use the builtin str() function to convert 
		adict's keys and values to strings.
    """
    new_list = []
    for key, value in adict.items():
        pair = str(key) + str(value)
        new_list.append(pair)
    return new_list

def get_N_random_elements_from_list(alist, N):
    """
    Returns a new list that chooses N elements randomly from alist,
    using the random.choice function, which can choose the same element more 
    than once.
    The resulting list that is returned should have N elements in it.
    """
    counter = 0
    new_list = []
    while counter < N:
        random_element = random.choice(alist)
        new_list.append(random_element)
        counter = counter + 1
    return new_list