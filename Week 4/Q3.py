'''     Given a list of numbers. Write a program to turn every item of a list into its square.     '''


# Prompt the user to input a list of numbers separated by spaces
user_input = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of integers
number_list = list(map(int, user_input.split()))

# Print the original list of numbers
print("Original list:", number_list) 

# Initialize an empty list to store the squared numbers
squared_list = []

# Loop through each number in the original list
for i in number_list:
    
    # Calculate the square of the current element
    squared_value = i * i
    
    # Append the squared value to the squared_list
    squared_list.append(squared_value)

# Print the list of squared numbers
print("Squared list:", squared_list)

