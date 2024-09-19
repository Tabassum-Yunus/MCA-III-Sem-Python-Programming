
'''     Given a two list of numbers, write a program to create a new list such that the new list 
        should contain odd numbers from the first list and even numbers from the second list.    '''



# Prompt the user to input a first list of numbers separated by spaces
user_input = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of integers
list1 = list(map(int, user_input.split()))

# Prompt the user to input a second list of numbers separated by spaces
user_input1 = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of integers
list2 = list(map(int, user_input1.split()))

# Initialize an empty list to store the required elements
myList = []

# Loop through the first list
for i in list1:
    # Check if the number is odd
    if i % 2 != 0:
        # Add odd numbers to myList
        myList.append(i)  

# Loop through the second list
for i in list2:
    # Check if the number is even
    if i % 2 == 0:
        # Add even numbers to myList
        myList.append(i)  

# Print the merged list containing odd numbers from the first list and even numbers from the second list
print('Merged list: ', myList)
