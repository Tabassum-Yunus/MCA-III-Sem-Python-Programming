'''     Write a program to read five real numbers from user and find the average and standard deviation.        '''

# Importing the math module and aliased as mt to use mathematical functions like sqrt
import math as mt

# Prompt the user to input a list of numbers separated by spaces
user_input = input('Enter list of numbers separated by space: ')

# Converting the input string into a list of floats using map() and split()
list1 = list(map(float, user_input.split()))

# Initializing variables to calculate sum, average, and variance
sum = avg = variance = 0

# Looping through the list to calculate the sum of all elements
for i in list1:
    sum += i

# Calculating the average (mean) by dividing the sum by the number of elements in the list
avg = sum / len(list1)

# Printing the calculated average
print('Average of numbers: ', avg)

# Looping through the list again to calculate the variance
# Variance is calculated by summing up the squared differences of each element from the average
for i in list1:
    variance += (i - avg) ** 2

# Calculating the standard deviation
# The variance is divided by the number of elements to get the mean of squared differences
# The square root of this value gives the standard deviation
std_deviation = mt.sqrt(variance / len(list1))

# Printing the calculated standard deviation
print('Standard deviation of numbers: ', std_deviation)
