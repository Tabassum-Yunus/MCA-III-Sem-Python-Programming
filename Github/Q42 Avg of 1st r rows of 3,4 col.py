'''     Write a python program to find the average value of the first 5 rows of the third 
        and fourth columns of a 2D numpy array.'''

import numpy as np
arr = np.random.randint(1,36, (6,6))
print(arr)
print(arr[:5, 2:4])
print(np.mean(arr[:5, 2:4]))
