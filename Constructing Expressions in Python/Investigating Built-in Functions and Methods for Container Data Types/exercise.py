"""
Investigating Built-in Functions and Methods for Container Data Types
Author: Leon Shpaner
Date:   July 18, 2020

- Append the number 4 to alist using the list.append() method.
Remove the first instance of the number 2 from alist using the list.remove() 
method.

- Use the list.index() method to find the position of the element 3 in alist.

-Now try appending the number 4 to aset. Note that this produces an error, 
which you will be quizzed about.

"""
# In the code editor, create a list named alist that contains the elements 
# 4,2,3,1 (in that order).
alist = [4,2,3,1]

# Use the built-in function len() to compute the length of alist, and assign 
# the result to the variable alist_len.

3 in alist
alist_len = len(alist)

# Use the function min() to return the smallest element of your list, and assign
# it to alist_min.
alist_min = min(alist)

# Use the function sorted() to return a numerically sorted version of your list,
# and assign the result to the variable sorted_alist.
sorted_alist = sorted(alist)

# Use the print function to print out both alist and sorted_alist and note 
# whether the order of both is the same.
print(alist)
print(sorted_alist)

# Create a set named aset that contains the numbers 4,2,3,1.
aset = {4,2,3,1}
3 in aset

# Use the built-in function len() to compute the length of aset, and assign the 
# result to the variable aset_len.
aset_len = len(aset)

# Use the function min() to return the smallest element of your set, and 
# assign it to aset_min.
aset_min = min(aset)

# Create a dictionary named adict that maps ‘a’ to 1, ‘b’ to 2, and ‘c’ to 3.
adict = {'a':1, 'b': 2, 'c':3}
3 in adict
'c' in adict

# Use the built-in function len() to compute the length of adict, and 
# assign the result to adict_len.
adict_len = len(adict)

# Use the function min() to compute the smallest element of adict, and assign it 
# to adict_min.
adict_min = min(adict)

# Test whether the number 3 is in the list you created, and assign the result to
#  list3.
list3 = True

# Test whether the number 3 is in the set you created, and assign the result 
# to set3.
set3 = True

# Test whether the number 3 is in the dictionary you created, and assign the 
# result to dict3.
dict3 = False

# Test whether the string ‘c’ is in the dictionary you created, and assign the 
# result to dictc.
dictc = True

# Append the number 4 to alist using the list.append() method.
alist.append(4)

# Remove the first instance of the number 2 from alist using the list.remove() 
# method.
alist.remove(2)

# Use the list.index() method to find the position of the element 3 in alist.
alist.index(3)

# Now try appending the number 4 to aset. Note that this produces an error, 
# which you will be quizzed about.
aset.append(4)