
'''     Write a program to find the sum of digits of a supplied integer.    '''

# Prompt a user to enter an input and convert it into integer
no = int(input("Enter an integer: "))

# Store the original number for later use
num = no

# Initialize sum of digits to 0
sum = 0

# Initialize remainder to 0
rem = 0

# Loop to count the sum of digits of number
while( no!=0):
    # Get the last digit from the original number
    rem = no%10

    # Add remainder to sum
    sum += rem

    # Remove the last digit from the original number
    no //= 10

# Print the sum of digits of an integer
print("Sum of digits of",num,":",sum)