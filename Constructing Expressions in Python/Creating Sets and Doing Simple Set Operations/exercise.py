"""
Creating Sets and Doing Simple Set Operations
Author: Leon Shpaner
Date:   July 17, 2020

- Write a Python expression that computes the elements that are in Region A of 
the Venn Diagram, and assign the result to the variable regionA.

- Write a Python expression that computes the elements that are in Region B of 
the Venn Diagram, and assign the result to the variable regionB.

- Write a Python expression that computes the elements that are in Region C of 
the Venn Diagram, and assign the result to the variable regionC.

- Write a Python expression that computes the elements that are in any Region 
of the Venn Diagram, and assign the result to the variable regionABC.
"""

my_marbles = {'black', 'green', 'blue', 'red', 'purple', 'yellow', 'cyan'}

your_marbles = {'green', 'magenta', 'red', 'brown', 'black', 'gray'}

print (my_marbles & your_marbles)

regionA = {'blue','purple','yellow', 'cyan'}
regionB = {'red','black','green'}
regionC = {'magenta','brown','gray'}
regionABC = {'black', 'blue', 'red', 'purple', 'yellow', 'cyan', 'green', 
'magenta', 'brown', 'gray'}
