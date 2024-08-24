'''     Write a program to remove characters from a string starting from n to last and
        return a new string.    '''

def remove_chars(str1, indx):
    # Slice the string from the start up to the specified index
    return str1[:indx]
    
# Prompt the user to enter a string
str = input('Enter String: ')

# Prompt the user to enter index from where characters should be removed
indx = int(input('Enter index from where characters to be removed: ')) 

# Print the original string
print('Original string: ', str)

# Call the function to remove characters from the specified index
strr = remove_chars(str, indx-1)

# Print the string after removal of characters
print('String after removal of characters: ', strr)
