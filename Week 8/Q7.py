'''     Write a Python program to create a list of user's supplied distinct integers having even number
        of elements. The program further creates two lists of equal lengths based on the original list,
        where first list is having all elements less than elements of second list. Display both the lists.      '''

# Import the copy module to create a deep copy of the list
import copy as c

# Input a list of integers from the user, using map to convert input into integers
# and split() to separate them by spaces
l = list(map(int, input('Enter list of integers: ').split()))

# Make a deep copy of the list `l` to avoid modifying the original list
a = c.deepcopy(l)

# Sort the copied list to find the middle element
a = sorted(a)

# Initialize two empty lists: one for elements less than the middle element,
# and another for elements greater than or equal to the middle element
first_list = []
second_list = []

# Find the middle element of the sorted list
# len(a)//2 gives the index of the middle element
mid = a[len(a)//2]

# Iterate over each element in the original list `l`
for i in l:
    # If the element is less than the middle element, append it to first_list
    if(i < mid):
        first_list.append(i)
    # Otherwise, append it to second_list (for elements >= mid)
    else:
        second_list.append(i)

# Print the first list containing elements less than the middle element
print('First list: ', first_list)

# Print the second list containing elements greater than or equal to the middle element
print('Second list: ', second_list)
