"""
Creating Lists and Assigning Them to Variables
Author: Leon Shpaner
Date:   July 19, 2020

Examine the code that’s been prepopulated in exercise1.py, and spend some time reading through it and the associated comments. 
You should see that the there are 3 main sorts of things going on to calculate the average value of my_list:

- Initializing some variables to store the running total of the list elements and how many elements there are
- Looping over the elements of my_list to increment the total and num_elements counter
- Dividing the total by num_elements to get the average

Fortunately, because there are built-in functions both for summing the elements of a list and computing its length, 
we can make shorten this code considerably.

In the code editor, below where the existing code is situated, write a one-line expression that sums the elements of 
my_list, divides it by the length of my_list, and assigns the result to a new variable called my_list_average. Print my_list_average.

"""
# Let's define a list of numbers and assign it to my_list
my_list = [10,20,30,40]

# Set a running total for elements in the list, initialized to 0
total = 0
# Set a counter for the number of elements in the list, initialized to 0
num_elements = 0

# Loop over all the elements in the list
for element in my_list:
    # Add the value of the current element to total
    total = total + element
    # Add 1 to our counter num_elements
    num_elements = num_elements + 1

# Compute the average by dividing the total by num_elements
average = total / num_elements

my_list_average = total/len(my_list)
print(my_list_average)