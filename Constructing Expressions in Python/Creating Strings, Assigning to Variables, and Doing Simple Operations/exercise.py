"""
Creating Strings, Assigning to Variables, and Doing Simple Operations
Author: Leon Shpaner
Date:   July 18, 2020
"""

# In the code editor, create a string 'abc' and assign it to the variable s1
s1 = 'abc'

# Create a string '123' and assign it to the variable s2
s2 = '123'

# Use the + operator to concatenate the strings s1 and s2, and assign the result 
# to the variable s3
s3 = s1+s2

# Print the value of s3
print(s3)

# Extract the item at position 0 of the string s3, and assign it to the variable
# pos0
pos0 = s1[0]

# Print the value of pos0
print(pos0)

# Extract the item at position 2 of the string s3, and assign it to the variable
# pos2
pos2 = s3[2]

# Print the value of pos2
print(pos2)

# The concatenated string s3 has '123' immediately following 'abc'. Write an 
# expression to create a new string with a space between 'abc' and '123', and 
# assign the result to a variable named s4.
s4 = s1+' '+s2
