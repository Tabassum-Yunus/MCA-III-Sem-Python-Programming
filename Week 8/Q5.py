'''     Write a python program that reads a string which contains English alphabets and numbers. 
        The program should create two lists L1 and L2, where L1 includes all the numbers present 
        in the string while L2 includes all the alphabets of the string.      '''

# Accept input string from the user
str = input('Enter string: ')

# Initialize two empty lists to store alphabets and numbers separately
alphabets = []
numbers = []

# Loop through each character in the input string
for i in str:
    # Try to convert the character to an integer (for digits)
    try:
        # If it's a number, append it to the 'numbers' list
        numbers.append(int(i))

    # If an error occurs (i.e., the character is not a number), handle it in the except block
    except:
        # Check if the character is an alphabet
        if(i.isalpha()):
            # If it's an alphabet, append it to the 'alphabets' list
            alphabets.append(i)

# Print the original string
print('Original string: ', str)

# Print the list containing all the numbers extracted from the string
print('List containing all the numbers of string: ', numbers)

# Print the list containing all the alphabets extracted from the string
print('List containing all the alphabets of string: ', alphabets)
