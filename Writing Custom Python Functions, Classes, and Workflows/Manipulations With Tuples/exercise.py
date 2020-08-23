"""
Manipulations With Tuples
Author: Leon Shpaner
Date:   August 14, 2020

One common situation where tuples are used to bundle related data in a specific 
order occurs when we want to return multiple values from a function. We’ve 
already seen an example of this with the function sum_and_difference(x, y), 
which returns both the sum and the difference of two inputs x and y. Inspect the
starter code in the editor window; you should see this function defined.
We can return multiple data elements in a tuple either by listing them in a 
comma-separated sequence as in the starter code, or by enclosing them in 
parentheses (i.e., as (x+y, x-y). Because the object that is returned by the 
function is a tuple, any variable that is assigned to the result of that 
function call is also a tuple.

We can either assign that result to a single variable (of type tuple), or we can
unpack the values in the tuple directly into multiple variables.
For example, we could either write result = sum_and_difference(10, 2) 
(in which case the sum would be the first element of the result tuple, and the 
difference the second), or we can write xysum, 
xydiff = sum_and_difference(10, 2).
If you are unpacking a tuple directly into multiple variables, however, you need
to make sure that you have as many variables on the left-hand side of the 
assignment as there are elements in the tuple on the right-hand side.
We’ve seen tuple unpacking before when we accessed the key-value pairs from a 
dictionary D; when we write something like for k,v in D.items(), we are 
unpacking a (key, value) tuple each time through the loop and assigning those 
values to the variables k and v, respectively.
"""

def sum_and_difference(x,y):
    return x+y, x-y

# In the code editor, write a new function called product_and_ratio(x, y) that 
# returns both the product of x and y (i.e., the result of multiplying them) and
# the ratio of x to y (i.e., the result of dividing the first argument by the 
# second). Test out your function in the interpreter.

def product_and_ratio(x, y):
    return x*y, int(x/y)
