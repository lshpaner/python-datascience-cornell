"""
Basic Exception Handling
Author: Leon Shpaner
Date:   August 9, 2020

Exceptions are errors generated at runtime based upon the values of particular 
variables; that is, they are different than syntax errors which are always wrong 
and which can be detected when you try loading the code. By anticipating certain 
types of exceptions that might get generated, you can write more robust code. 
he main Python keywords for dealing with exceptions are try and except: first 
you try something in one indented code block, and if that throws an exception, 
you add some more code in the except codeblock to deal with that case.
"""

# Examine the starter code in the editor; in particular, the first function 
# named add. It looks similar to some other code you’ve worked with, in that it 
# takes two inputs and returns their sum. We know that we can add two numbers 
# using the + operator, and we also know that we can add two strings with the + 
# operator.

def add(x,y):
    """
    Returns the sum of inputs x and y
    """
    result = x + y
    return result

# Run the starter code in the interpreter.
# Try the add function for two numbers; enter and execute add(2,3). It should 
# return the result 5.
# Try the add function for two strings; enter and execute add('abc','def'). It 
# should return the result 'abcdef'.
# Try the add function for a number and a string; enter and execute 
# add(2,'abc'). 
# You should notice that an error is generated, noting that you cannot use the +
# operator between 'int' and 'str'.

"""
Now we want to fix the code to deal with additions between types that are not 
supported. We’ll do that by defining a new function named add2. The code in add 
works well if the + operator can be used with the inputs x and y, so we want to 
keep that, but put it in a try block. 
"""

# There is some missing code in add2 that you’ll need to fill in:

"""
- the except statement requires you to identify the specific exception you are 
trying to catch – see QUESTION #1 on Page 1.
"""

# within the except block, you’ll want to fill out the rest of the missing 
# pieces based on what is documented in the docstring 
# (note: return None returns the Python object None, and is equivalent to 
# return; in fact, a function that omits a return statement entirely also 
# returns None).

def add2(x,y):
    """
    Returns the sum of inputs x and y if they can be added,
    and otherwise returns None and prints the statement:
    "Those two inputs cannot be added to each other."
    """
    try:
        result = x + y
        return result
    except TypeError:
        print("Those two inputs cannot be added to each other.")
        return None
    