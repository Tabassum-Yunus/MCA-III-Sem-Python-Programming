'''     Swap two numbers using XOR      '''


# Take two integers as input from the user.
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

# Output: Print the values of a and b before swapping.
print('Before swapping a:', a, 'and b:', b)

# Swapping logic using XOR:

# Step 1: XOR a and b, store the result in a
a = a ^ b 

# Step 2: XOR new a (which is a ^ b) with b to get original a, store in b
b = a ^ b  

# Step 3: XOR new a (which is a ^ b) with new b (which is original a) to get original b, store in a
a = a ^ b  

# Output: Print the values of a and b after swapping.
print('After swapping a:', a, 'and b:', b)
