"""
Creating Strings, Assigning to Variables, and Doing Simple Operations
Author: Leon Shpaner
Date:   July 18, 2020

Append the number 4 to alist using the list.append() method.
Remove the first instance of the number 2 from alist using the list.remove() method.
Use the list.index() method to find the position of the element 3 in alist.
Now try appending the number 4 to aset. Note that this produces an error, which you will be quizzed about.

"""

alist = [4,2,3,1]
3 in alist
alist_len = len(alist)
alist_min = min(alist)
sorted_alist = sorted(alist)
aset = {4,2,3,1}
3 in aset
aset_len = len(aset)
aset_min = min(aset)
adict = {'a':1, 'b': 2, 'c':3}
3 in adict
'c' in adict
adict_len = len(adict)
adict_min = min(adict)
list3 = True
set3 = True
dict3 = False
dictc = True
alist.append(4)
alist.remove(2)
alist.index(3)
aset.append(4)