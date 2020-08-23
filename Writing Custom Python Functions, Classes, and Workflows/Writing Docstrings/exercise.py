# In the code editor, add the following docstring to the function 
# add_two_strings_with_separator. Remember that the docstring is part of the 
# function definition and therefore must be indented appropriately.

"""
Returns the concatenation of the first string and the second string, 
separated by the separator.
"""

def add_two_strings_with_separator(first, second, separator):

    """
    Returns the concatenation of the first string and the second string, 
    separated by the separator.
    """
    
    result = first + separator + second
    return result

# In the code editor, add the following docstring to the function
# add_two_strings and inspect the docstring in the interpreter:
"""
Returns the concatenation of the first string and the second string, 
separated by the separator (default=' ').
"""
def add_two_strings(first, second, separator=' '):
    """
    Returns the concatenation of the first string and the second string, 
    separated by the separator (default=' ').
    """
    
    result = first + separator + second
    return result
