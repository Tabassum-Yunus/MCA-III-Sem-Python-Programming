'''     Write a python program to find the maximum of average value in each row of a 2D numpy array.    '''

import numpy as np
row = 0
arr = np.random.randint(1,36, (6,6))
print(arr)
print(np.mean(arr, axis=0))
print(max(np.mean(arr, axis=0)))
