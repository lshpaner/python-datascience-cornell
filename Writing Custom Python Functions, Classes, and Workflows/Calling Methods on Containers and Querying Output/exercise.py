"""
Calling Methods on Containers and Querying Output
Author: Leon Shpaner
Date:   August 14, 2020

"""
# Examine the starter code in the editor window, which defines two dictionaries.


dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

dict2 = {'c': 10, 'd': 20, 'e': 30, 'f': 40, 'g': 50}

x = {'a','b','c','d','e'}
y = {'c','d','e','f','g'}

# In the code editor:
# write an expression that computes which keys are shared between the two 
# dictionaries and stores it in the variable named shared_keys (hint: use set 
# intersection, to store the group of shared keys in a Python set).

shared_keys = x.intersection(y)
print(shared_keys)

# Write an expression that computes which values are shared between the two 
# dictionaries and stores it in the variable named shared_values.
z = {1,2,3,4,5}
zed = {10,20,30,40,50}
shared_values = z.intersection(zed)
print(shared_values)


