'''     Write a program to accept a string from the user and display characters that are
        present at an even index number.    '''


# Prompt the user to enter a string
str = input('Enter String: ')

# Print the message without moving to a new line
print('Characters in string at even index: ', end='')

# Loop through the string from index 1 and moving by steps of 2 to get characters at user's even index
for i in range(1, len(str), 2):
    # Print the character at the current index without a newline
    print(str[i], end='')