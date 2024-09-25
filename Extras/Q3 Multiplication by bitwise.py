'''     Write a program to read an integer and use bitwise operators to multiply it by 2 ( << operator ).   '''

# Taking an integer input from the user
num = int(input('Enter an integer: '))

# Taking another integer input for how many times the user wants to multiply by 2
times = int(input('Enter how many times you want to multiply it by 2: '))

# Using the left shift operator (<<) to multiply the number by 2 'times' times
result = num << times

# Printing the result of the multiplication
print(result)
