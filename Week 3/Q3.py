'''     Write a program to print characters from a string which are present at an even
        index numbers.     '''

# Define a string
str = 'Python Programming'

# Print the message without moving to a new line
print('Characters in string at even index: ', end='')

# Loop through the string from index 1 and moving by steps of 2 to get characters at user's even index
for i in range(1, len(str), 2):
    # Print the character at the current index without a newline
    print(str[i], end='')
