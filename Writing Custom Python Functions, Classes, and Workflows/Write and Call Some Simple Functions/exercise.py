"""
Write and Call Some Simple Functions
Author: Leon Shpaner
Date:   August 7, 2020

The code includes three different instances of testing which is the smaller of 
two variables and assigning that value to a new variable.
"""
# In the code editor, write a function named find_min that takes two inputs and 
# returns the lesser of the two. Remember to use the def keyword to start the 
# definition of a new function, indent the body of the function under the def 
# line, and return the result at the end.

def find_min(x,y):
    
    if x < y:
        min_xy = x
    else:
        min_xy = y
    
    print(min_xy)
    
    return min_xy

x = 3
y = 4
   
# Call find_min with the variables x and y as arguments and assign the returned 
# value to the new variable min_xy.
min_xy = find_min(x,y) 

def find_min(a,b):
    
    if a < b:
        min_ab = a
    else:
        min_ab = b

    print(min_ab)
    
    return min_ab

a = 12.3
b = 13.7


min_ab = find_min(a,b) 

def find_min(w,z):

    if w < z:
        min_wz = w
    else:
        min_wz = z

    print(min_wz)
    
    return min_wz

w = -3.9
z = -4.7

min_wz = find_min(w,z) 

# We are free to define more than one function in our code. In the code editor, 
# write a new function called find_max that takes two inputs and returns the 
# greater of the two.
def find_max(x,y):

    if x > y:
        max_xy = x
    else:
        max_xy = y

    print(max_xy)
    
    return max_xy

# Use your new function to find the greater of x and y and assign it to the 
# variable max_xy.
max_xy = find_max(x,y)



