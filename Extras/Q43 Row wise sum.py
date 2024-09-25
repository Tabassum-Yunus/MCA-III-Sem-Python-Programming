'''Write a python program to compute the row wise sum of all possible values in a 2D numpy array.'''

import numpy as np
arr = np.random.randint(1,36, (6,6))
print(arr)
print(np.sum(arr, axis=0))
