
'''     Write a program to count the total number of digits in a number using a while loop.     '''


# Prompt the user to enter a number and convert it into integer
no = int(input("Enter an integer: "))

# Store the original number for later use
num = no

# Initialize number of digigts to 0
d = 0

# Loop to count the number of digits
while( no!=0):
    # Increment number of digits by 1
    d += 1

    # Remove the last digit from the original number
    no //= 10

# Print the number of digits an integer has
print("No. of digits in",num,":",d)