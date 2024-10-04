'''     Write a python program to calculate row and columns wise mean of an array.    '''

import numpy as np  

# Input dimension of the array
rows = int(input('Enter no. of rows of array: '))  # Taking the number of rows as input from the user
columns = int(input('Enter no. of columns of array: '))  # Taking the number of columns as input from the user

# Create an array of random integers between 1 and 100 with shape (rows, columns)
arr = np.random.randint(1, 100, (rows, columns))

print('Array')
print(arr, '\n')  # Printing the generated array

# Calculate and print the row-wise mean (mean of elements along columns)
print('Row-wise mean:', np.mean(arr, axis=0))

# Calculate and print the column-wise mean (mean of elements along rows)
print('Column-wise mean:', np.mean(arr, axis=1))
