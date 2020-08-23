"""
Calling Functions Sequentially to Process Data
Author: Leon Shpaner
Date:   August 9, 2020

You’re going shopping, and need to calculate how much money you’ll need. Food 
items are not taxable, but all other items are taxable at 8%.
There is a group of food items you want to buy, which are listed along with 
their prices (in US dollars). There is also a group of non-food items that you 
want to buy.
"""

# Food items (prices in US dollars):

apples = 2.69
coffee = 8.99
bread = 2.99
lettuce = 3.19
cheese = 6.89

# Non-food items

pencils = 3.49
toothpaste = 3.89
shoelaces = 4.99
flowers = 7.99
soap = 1.29

# In the code editor:
# Write a Python expression to calculate the total cost of the nontaxable item1s
# (using the variables for each of the relevant items), and assign that total to
# the variable nontaxable.

nontaxable = apples+coffee+bread+lettuce+cheese

# Write a Python expression to calculate the total cost of the taxable items, 
# and assign that total to the variable taxable.
taxable = pencils+toothpaste+shoelaces+flowers+soap

# Write a Python expression to assign the current tax rate (8%) to a variable 
# named tax_rate.
tax_rate = 0.08

# Write a Python expression to calculate the total cost of all the items 
# (including tax), and assign it to a variable named total_cost, using the 
# intermediate variables that you have created.
tax1 = taxable * tax_rate
total_cost = taxable+tax1 + nontaxable
print(total_cost)

# The tax rate was increased to 9%.
# Add a new variable called new_tax_rate
new_tax_rate = 0.09
tax2 = taxable * new_tax_rate

# Compute the new cost of all your items & assign the result to new_total_cost.
new_total_cost = taxable+tax2 + nontaxable
print(new_total_cost)