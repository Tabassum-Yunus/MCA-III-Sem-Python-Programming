'''     Write a program create a numpy array and sort as per below cases:
            Case 1: Sort array by the second row.
            Case 2: Sort the array by the second column.'''

import numpy as np

# Create a 4x5 array with random integers between 1 and 10
arr = np.random.randint(1, 10, (4, 5))

# Print the original array
print('Original array:')
print(arr)

# Sorting the array based on the second row
# arr[1, :] accesses the second row
# argsort() returns the indices that would sort this row
# arr[:, arr[1, :].argsort()] reorders the columns of the array based on the sorted second row
print('Sorted array by second row:')
print(arr[:, arr[1, :].argsort()])

# Sorting the array based on the second column
# arr[:, 1] accesses the second column
# argsort() returns the indices that would sort this column
# arr[arr[:, 1].argsort(), :] reorders the rows of the array based on the sorted second column
print('Sorted array by second column:')
print(arr[arr[:, 1].argsort(), :])




