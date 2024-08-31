
'''     Write a program to pick a random character from a given String supplied by the user.       '''


# Import random module and aliased as r for easier usage in the code.
import random as r

# Prompt the user to enter a string.
str = input("Enter string: ")

                                                # Approach 1

# Use the choice() function to select a random character from the input string.
print("Random char of string using choice(): ", r.choice(str))


                                                # Approach 2

# Generate a random index within the range of the string's length.
index = r.randrange(len(str))

# Print the character at the random index from the string.
print("Random char of string using random(): ", str[index])
