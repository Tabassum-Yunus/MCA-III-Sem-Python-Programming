'''     Write a program to check if the given number is a palindrome number or not.     '''


# Prompt the user to enter an integer and convert it to an integer
num = int(input("Enter an integer: "))

# Initialize the reversed number to 0
rev = 0

# Store the original number for later comparison
o_num = num
 
# Loop to reverse the digits of the number
while (num != 0):
    # Get the last digit of the number
    rem = num % 10
    
    # Append the last digit to the reversed number
    rev = rev * 10 + rem
    
    # Remove the last digit from the original number
    num //= 10

# Print the reversed number
print("Reversed number: ", rev)

# Check if the original number is same as reversed number
if (o_num == rev):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

