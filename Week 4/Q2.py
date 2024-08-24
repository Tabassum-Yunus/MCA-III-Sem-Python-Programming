'''     Write a function to return True if the first and last number of a given list is
        same. If numbers are different then return False.       '''


# Check if the first and last numbers of the given list are the same.
def is_first_last_same(list):       # list (A list of numbers) is the parameter
    
    # Return True if the first and last numbers are the same, False otherwise.

    # Compare the first and last elements of the list
    return list[0] == list[-1]

# Prompt the user to input a list of numbers separated by spaces
user_input = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of integers and map it
number_list = list(map(int, user_input.split()))

# Call the function with user inputted list of numbers
result = is_first_last_same(number_list)

# Display the results
print("First and last number is same?:", result)
