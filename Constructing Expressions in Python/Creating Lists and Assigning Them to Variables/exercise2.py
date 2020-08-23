"""
Creating Lists and Assigning Them to Variables
Author: Leon Shpaner
Date:   July 12, 2020

- In addition to accessing list elements, you can also change them using the 
square brackets, by assigning a new value to a list element at a specified 
position.

- In exercise2.py in the code editor window, assign the item at position 2 in 
my_list to the string 'C', and add a new line of code to print my_list. Run the 
code file within the interpreter by executing %run exercise2.py.

- Lists are very flexible in what they can hold. They can hold a mix of objects 
of different types, including other lists.

- In the next line of exercise2.py in the code editor window, create a new list 
containing the objects 1, 2.01, '123', and the list [5,6,7] (in that order), and 
assign it to the variable my_second_list. Add a line of code to print the list, 
and rerun the code file in the interpreter.
"""

my_list = [1,2,3,4]

my_list[2] = 'C'
print(my_list)

# 

my_second_list = [1,2.01,'123',[5,6,7]]
print(my_second_list)
