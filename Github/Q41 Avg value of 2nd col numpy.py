'''     Write a python program to find the average value of the second column of a 2D numpy array.  '''

import numpy as np

arr = np.random.randint(1,24, (4,6))
print(arr)
print(arr[1:2])
print(np.mean(arr[1:2], axis=1))


'''
2D Array:
axis=0: Operates along rows (vertically). For example, np.sum(arr_2d, axis=0) calculates the sum of each column.
axis=1: Operates along columns (horizontally). np.sum(arr_2d, axis=1) calculates the sum of each row.
'''


