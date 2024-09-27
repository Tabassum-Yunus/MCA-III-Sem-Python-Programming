'''     Write a python program to create a Numpy array of NxN having random integers between 1 and 100. 
        The program further finds average values across both the diagonals  '''

import numpy as np

# Input dimension of the array
n = int(input('Enter dimension of array: '))

# Initialize variables to store the sum of the diagonals
diag1 = diag2 = 0

# Create an n x n array of random integers between 1 and 100
arr = np.random.randint(1, 100, (n, n))

# Loop to calculate the sum of the elements on the main diagonal and antidiagonal
for i in range(n):
    diag1 += arr[i, i]           # Get the elements of the main (leading) diagonal
    diag2 += arr[i, n - (i + 1)] # Get the elements of the antidiagonal (opposite diagonal)

# Print the generated array
print(arr)

# Print the average of the main diagonal
print('Average of leading diagonal: ', diag1 / n)

# Print the average of the antidiagonal
print('Average of antidiagonal: ', diag2 / n)
