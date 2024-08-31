'''     Given a two Python list. Write a program to iterate both lists simultaneously and display
        items from list 1 in original order and items from list 2 in reverse order.      '''


# Import itertools module and aliased as t for easier usage in the code.
import itertools as t

# Prompts the user to input a list of integers separated by spaces.
user_input1 = input("Enter list of integers separated by space: ")

# The input string is splitted using split() finction into individual components (based on spaces) 
# and then converted into a list of integers using map() function and then make a list using list().
list1 = list(map(int, user_input1.split()))

# Prompts the user to input a list of integers separated by spaces.
user_input2 = input("Enter list of integers separated by space: ")

# The input string is splitted using split() finction into individual components (based on spaces) 
# and then converted into a list of integers using map() function.
list2 = list(map(int, user_input2.split()))

# Use itertools.zip_longest() funtion to pair elements from list1 with the reversed list2.
# If the lists are of unequal length, 'fillvalue' is used to fill in the gaps.
for i, j in t.zip_longest(list1, list2[::-1], fillvalue=" "):
    
    # Print each pair of elements (i, j).
    print(i, j)







                                                # Another approach

# user_input1 = input("Enter list of integers separated by space: ")
# list1 = list(map(int,user_input1.split()))
# user_input2 = input("Enter list of integers separated by space: ")
# list2 = list(map(int,user_input2.split()))
# for i,j in zip(list1, list2[::-1]):             #  zip() function will stops when the shortest iterable(list) is exhausted.
#     print(i,j)




                                                # Another approach

# print("Number of elements in both the list must be same")
# user_input1 = input("Enter list of integers separated by space: ")
# list1 = list(map(int,user_input1.split()))
# user_input2 = input("Enter list of integers separated by space: ")
# list2 = list(map(int,user_input2.split()))
# for i in range(len(list1)):
#     print(list1[i], list2[len(list2)-i-1])




                                                
 