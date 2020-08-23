"""
Default Arguments
Author: Leon Shpaner
Date:   August 7, 2020

A function in Python takes a set of inputs, and acts on those inputs to produce 
an output. The values of all the inputs must be specified, or else Python will 
raise an error about missing arguments. In the previous exercise, we saw that we
needed to pass into a function as many “positional arguments” as are specified 
in the function definition. It is possible, however, to provide default values 
for one or more arguments in case those arguments are not passed into the 
function.

"""
# Now let’s write a function that lets us add any two strings in a similar 
# manner. In the code editor, define a function named 
# add_two_strings_with_separator that takes 3 inputs 
# (first, second, and separator). The function should return a combined string 
# with the separator included in the middle between the first and second strings.

myname = 'My' + ' ' + 'Name'

def add_two_strings_with_separator(first, second, separator):
    
    yourname = first + separator + second
    return yourname

# Test out your new function by writing the following expression in the code 
# editor and running the exercise in the interpreter: 
# yourname = add_two_strings_with_separator('Your', 'Name', ' '). You should 
# note that the last argument passed in to that function is a string that will 
# be used to separate the other two strings; it is a string consisting of a 
# single space. If you’ve done this correctly, then the variable yourname 
# should contain the string 'Your Name'.

yourname = add_two_strings_with_separator('Your', 'Name', ' ')

"""
Since we may usually want a single space to be used as the string separator, we 
can simplify things so that we do not have to specify the single space as a 
string separator every time we write a function call. This is where default 
arguments come in. We can make the string separator a default argument, and 
assign it the default value of a single space ' '.
"""

#Now define a new function called add_two_strings that returns the same 
# concatenated and separated strings as before. This time however, the function 
# will take 2 positional arguments (first and second) and 1 default argument 
# (separator, which is assigned a default value of ' ').

def add_two_strings(first ='First', second = 'Second' , separator=' '):

    hername = first + separator + second 
    
    return hername
# Call add_two_strings with two arguments:
# Test your code by calling your function to create a new variable called 
# hername which will contain the value of the concatenation of 'Her' and 'Name' 
# with a space in between. Do not pass in a value for the separator.
hername = add_two_strings('Her', 'Name')
print(hername)

# Call add_two_strings with three arguments:
# Even though the separator has a default value, you can always choose to 
# override that default value by passing in a third argument to your function. 
# Call your function to create a new variable called her_name, where the strings
#  'Her' and 'Name' are joined with an underscore '_' in between them. Hint: 
# This time, you should pass in a value for the separator '-'.

her_name = add_two_strings('Her','Name','_')
print(her_name)

# In the code editor, write two expressions that call your previous function as 
# follows, and run exercise.py in the interpreter:
result1 = add_two_strings(first='My', second='Name')
result2 = add_two_strings(second='My', first='Name')
print(result1)
print(result2)
