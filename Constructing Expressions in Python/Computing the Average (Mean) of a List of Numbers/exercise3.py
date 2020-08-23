"""
Creating Lists and Assigning Them to Variables
Author: Leon Shpaner
Date:   July 19, 2020

In exercise3.py in the code editor window, create a new list containing a 
mixture of letters and numbers: my_other_list = [1, 2.3, 'a', 4.7, 'd'], and 
write an expression computing its average value using a similar expression as 
the one you previously wrote, storing the result in my_other_list_average.
"""
my_other_list = [1, 2.3, 'a', 4.7, 'd']
# Set a running total for elements in the list, initialized to 0
total = 0
# Set a counter for the number of elements in the list, initialized to 0
num_elements = 0

# Loop over all the elements in the list
for element in my_other_list:
    # Add the value of the current element to total
    total = total + element
    # Add 1 to our counter num_elements
    num_elements = num_elements + 1

# Compute the average by dividing the total by num_elements
average = total / num_elements
my_other_list_average= total/len(my_other_list)