
'''     Write a Program to extract each digit from an integer in the reverse order     '''


# Prompt the user to enter a number and convert it into integer
num = int(input("Enter a no.: "))

# Initialize a variable to hold the remainder
rem = 0

# Print the supplied string without moving to a next line
print("Reversed no.: ", end="")

# Loop to find reverse of number
while(num!=0):
    # Get the last digit of num
    rem = num % 10
    
    # Remove the last digit from num
    num //= 10
    
    # Print the digit stored in rem without moving to a new line
    print(rem,end="")
