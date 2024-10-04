'''     Write a python program to create a Numpy array of NxN having random integers between 1 and 100. 
        The program further finds average values across both the diagonals  '''

import numpy as np

# Input dimension of the array
n = int(input('Enter dimension of array: '))

# Initialize variables to store the sum of the diagonals
main_diagonal = anti_diagonal = 0

# Create an n x n array of random integers between 1 and 100
arr = np.random.randint(1, 100, (n, n))

# Loop to calculate the sum of the elements on the main diagonal and antidiagonal
for i in range(n):
    main_diagonal += arr[i, i]           # Get the elements of the main (leading) diagonal
    anti_diagonal += arr[i, n - (i + 1)] # Get the elements of the antidiagonal (opposite diagonal)

# Print the generated array
print(arr)

# Print the average of the main diagonal
print('Average of leading diagonal: ', main_diagonal / n)

# Print the average of the antidiagonal
print('Average of antidiagonal: ', anti_diagonal / n)
