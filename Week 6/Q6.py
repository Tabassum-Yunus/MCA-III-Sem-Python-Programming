'''     Write a program to accept a string and display the following:
            a. Number of uppercase characters
            b. Numbers of lowercase characters
            c. Total number of alphabets
            d. Number of digits     '''


# Accept input string from the user
str = input('Enter string: ')

# Initialize counters for uppercase, lowercase, alphabets, and digits
upper = lower = alpha = digits = 0

# Loop through each character in the input string
for i in str:
    # Check if the character is uppercase
    if i.isupper():
        upper += 1
    
    # Check if the character is lowercase
    elif i.islower():
        lower += 1
    
    # Check if the character is an alphabet (upper or lowercase)
    if i.isalpha():
        alpha += 1
    
    # Check if the character is a digit
    elif i.isdigit():
        digits += 1 

# Print the results
print('Number of uppercase characters: ', upper)
print('Number of lowercase characters: ', lower)
print('Total number of alphabets: ', alpha)
print('Number of digits: ', digits)
