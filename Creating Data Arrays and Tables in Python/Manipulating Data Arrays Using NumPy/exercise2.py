import numpy as np
a = np.array([[0,1,2,3], [4,5,6,7], [8,9,10,11]])
print(a)

lastrow = a[2]

firstcol = a[:,0]
print(len(firstcol))

a_gt_5 = a > 5
print(a_gt_5)

elements_gt_5 = a[a_gt_5]
print(elements_gt_5)