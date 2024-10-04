'''     Write a python program to create a list of users supplied words. The program further creates
        two lists based on the original list, where first list is having all words, whose length is
        less than or equal to the average length of the words, while 2nd list contains all words whose
        length is greater than the average length. Display both the list.   '''


# Input a string from the user
str = input('Enter string: ')  # Prompt the user to enter a string

# Split the input string into a list of words
list = str.split()  # Split the string by whitespace into a list of words

# Initialize lists to store words based on their length comparison to the average
greater_list = []  # List to hold words longer than the average length
smaller_equal_list = []  # List to hold words shorter than or equal to the average length
chars_in_list = 0  # Variable to count the total number of characters in all words

# Calculate the total number of characters in the words
for i in list:
    chars_in_list += len(i)  # Increment the total character count by the length of each word

# Calculate the average length of the words
avg_length = chars_in_list // len(list)  # Integer division to get the average length

# Separate words into greater or smaller/equal based on average length
for i in list:
    if len(i) > avg_length:  # If the length of the word is greater than the average
        greater_list.append(i)  # Add to greater_list
    else:  # If the length of the word is less than or equal to the average
        smaller_equal_list.append(i)  # Add to smaller_equal_list

# Print the original string and the resulting lists
print('Original string: ', str)  # Display the original string
print('List having words with length > average length: ', greater_list)  # Display words longer than the average
print('List having words with length <= average length: ', smaller_equal_list)  # Display words shorter or equal to the average
