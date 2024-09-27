'''     Write a python program to create a Numpy array of NxN having random integers between 1 and 100. 
        The program further finds average values across both the diagonals  '''

import numpy as np

# Input dimension of the array
n = int(input('Enter dimension of array: '))

# Create an n x n array of random integers between 1 and 100
arr = np.random.randint(1, 100, (n, n))

# Print the original array
print('Original array:\n', arr)

# Extract and print the main diagonal (top-left to bottom-right)
main_diagonal = np.diagonal(arr)
print('Main diagonal: ', main_diagonal)

# Extract and print the anti-diagonal (top-right to bottom-left)
anti_diagonal = np.fliplr(arr).diagonal()
print('Anti diagonal: ', anti_diagonal)

# Calculate and print the average of the main diagonal
print('Average of main diagonal: ', np.mean(main_diagonal))

# Calculate and print the average of the anti-diagonal
print('Average of anti diagonal: ', np.mean(anti_diagonal))
