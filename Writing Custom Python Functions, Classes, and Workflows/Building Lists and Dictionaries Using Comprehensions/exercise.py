"""
Building Lists and Dictionaries Using Comprehensions
Author: Leon Shpaner
Date:   August 14, 2020
"""

# The function extract_even_numbers_in_list extracts the elements of a list that
# are even. The list my_evens has been created by calling this function on 
# my_list. Inspect the data in my_evens.

my_list = [1, 3, 14, 22, 29, 43, 89, 102, 256]

def extract_even_numbers_in_list(alist):
    """
    Returns a list of the numbers in the input alist
    that are even numbers

    NOTE: n%2 == 0 if n is even,  n%2 == 1 if n is odd
    """
    result = []
    for elem in alist:
        if elem%2 == 0:
            result.append(elem)
    return result

my_evens = extract_even_numbers_in_list(my_list)

# Create a new list called my_evens2 by using a list comprehension that does the
# same thing as extract_even_numbers_in_list, but all in one line.
my_evens2 = [elem for elem in my_list if elem % 2 == 0]
s = 'The answer is 42, but many people guess 12.'

# The function extract_digits_from_string extracts the characters in a string 
# that are digits. In this function, the method string.is_digit is used to test 
# whether or not a string is a digit (or collection of digits). The list 
# str_digits has been created by calling this function on the supplied string s.
# Inspect the data in str_digits.

def extract_digits_from_string(s):
    """
    Returns a list of all the digits that appear in a string,
    in the order in which they are encountered.
    """
    result = []
    for c in s:
        if c.isdigit():
            result.append(c)
    return result

str_digits = extract_digits_from_string(s)

# Create a new list called str_digits2 by using a list comprehension that does 
# the same thing as extract_digits_from_string, but all in one line.
str_digits2 = [c for c in s if c.isdigit()]

# The function make_dict_of_squares creates a dictionary that maps from integers
# to their squares, starting with 0 and ending at one less than the input n. The
# dictionary squares has been created by calling this function with the input 
# 10. Inspect the data in squares. Since it is a dictionary, it contains both 
# keys and values.

def make_dict_of_squares(n):
    """
    Returns a dictionary that maps from integers to their squares, 
    starting with 0 and ending at one less than the input n
    """
    result = {}
    for i in range(n):
        result[i] = i*i
    return result

squares = make_dict_of_squares(10)

# Create a new dictionary called squares2 by using a dictionary comprehension 
# that does the same thing as make_dict_of_squares, but all in one line. Recall 
# that dictionary comprehensions are constructed using curly brackets, with each
# key and value in a pair separated by a colon :.
squares2 = {n: n**2 for n in range(10)}