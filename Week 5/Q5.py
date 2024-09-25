'''     Write a program to create a numpy array and return array of odd rows and even
        columns from the numpy array.   '''



# Import numpy module and aliased as np for easier usage in the code.
import numpy as np

# creating a numpy array with elements from 0 to 35
array = np.arange(36)

# Set the dimaension of the array to 6x6
array.shape = (6,6)

# Printing the original array
print('Original array: ', array)

# Extracting odd rows (1st, 3rd rows, etc. are indexed as 1, 3)
odd_rows = array[1::2]  # Start from index 1, take every 2nd row
    
# Extracting even columns (0th, 2nd, 4th columns, etc.)
even_columns = odd_rows[:,::2]  # Take all rows and every 2nd column

print('Required array of odd rows and even columns from original array: ')
print(even_columns)





















