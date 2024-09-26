'''     Write a python program to find the maximum value in each row of a 2D numpy array.   '''

import numpy as np
row = 0
arr = np.random.randint(1,36, (6,6))
print(arr)
print('Max values in each row')
for i in arr:
    print(row,':',max(i))
    row += 1
