"""
Creating Lists and Assigning Them to Variables
Author: Leon Shpaner
Date:   July 19, 2020

In exercise2.py in the code editor window, create the set of numbers my_set = 
{40, 20, 30, 10}, and write an expression computing its average value using a 
similar expression as the one you previously wrote, storing the result in the 
variable my_set_average.
"""

my_set = {40, 20, 30, 10}
# Set a running total for elements in the list, initialized to 0
total = 0
# Set a counter for the number of elements in the list, initialized to 0
num_elements = 0

# Loop over all the elements in the list
for element in my_set:
    # Add the value of the current element to total
    total = total + element
    # Add 1 to our counter num_elements
    num_elements = num_elements + 1

# Compute the average by dividing the total by num_elements
average = total / num_elements
my_set_average = total/len(my_set)