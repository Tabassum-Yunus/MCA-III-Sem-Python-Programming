'''     Write a program create a numpy array and sort as per below cases:
            Case 1: Sort array by the second row.
            Case 2: Sort the array by the second column.'''

import numpy as np

arr = np.random.randint(1,10,(5,5))
print('Original array')
print(arr)

print('Sorted array by second row')
print(np.sort(arr[:,arr[1:2]]))

print('Sorted array by second coulumn')
print(np.sort(arr[:, 1:2]))