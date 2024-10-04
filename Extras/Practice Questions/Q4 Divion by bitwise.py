'''     Write a program to read an integer and use bitwise operators to divide it by 4 (>> operator ).      '''

# Taking an integer input from the user
num = int(input('Enter an integer: '))

# Taking another integer input for how many times the user wants to divide the number by 4
times = int(input('Enter how many times you want to divide number by 4: '))

# Using the right shift operator (>>) to divide the number by 4 'times' times
result = num >> times*2

# Printing the result of the division
print(result)


