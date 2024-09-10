'''     Swap two numbers using + and -      '''

# Take two integers as input from the user.
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

# Output: Print the values of a and b before swapping.
print('Before swapping a:', a, 'and b:', b)

# Swapping logic using arithmetic operations:

# Step 1: Add a and b, and store the result in a
a = a + b  

# Step 2: Subtract b from new a to get the original a, and store it in b
b = a - b  

# Step 3: Subtract new b (which is original a) from new a to get the original b, and store it in a
a = a - b  

# Output: Print the values of a and b after swapping.
print('After swapping a:', a, 'and b:', b)
