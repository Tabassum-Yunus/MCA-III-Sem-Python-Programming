'''     Check if the number is odd or even using bitwise operator     '''

# Prompt the user to enter an integer
no = int(input('Enter a number: '))


# The bitwise AND operation with 1 (`no & 1`) checks the least significant bit
# If the result is 1, the number is odd; if the result is 0, the number is even
if (no & 1) == 1:

    # Print statement if the number is odd
    print(no,'is odd')   
else:

    # Print statement if the number is even
    print(no,'is even')  