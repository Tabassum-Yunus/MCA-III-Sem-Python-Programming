'''     Write a Python program that inputs two tuples and creates a third that contains
        all elements of the first followed by all elements of the second.      '''


# Prompt the user to input a first list of numbers separated by spaces
user_input = input("Enter a first list of numbers separated by spaces: ")

# Convert the input string into a tuple of integers
tup1 = tuple(map(int, user_input.split()))

# Prompt the user to input a first list of numbers separated by spaces
user_input1 = input("Enter a second list of numbers separated by spaces: ")

# Convert the input string into a tuple of integers
tup2 = tuple(map(int, user_input1.split()))

# Concatenate both tuples and assigned to a new tuple
new_tup = tup1+tup2

# Print the concatenated tuple
print(new_tup)
