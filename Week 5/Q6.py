'''     Write a program create a numpy array and sort as per below cases:
            Case 1: Sort array by the second row.
            Case 2: Sort the array by the second column.'''

import numpy as np

arr = np.random.randint(1,10,(4,5))
print('Original array')
print(arr)

print('Sorted array by second row')
print(arr[:,arr[1,:].argsort()])

print('Sorted array by second coulumn')
print(arr[arr[:,1].argsort(),:])



