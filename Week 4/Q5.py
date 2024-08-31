'''     Write a program to count the number of occurrences of item 50 from below tuple tp1:
        tp1= (50, 10, 60, 70, 50)       '''


# Prompt the user to input a list of integers separated by spaces.
user_input = input("Enter list of integers separated by space: ")

# The input string is splitted using split() finction into individual components (based on spaces) 
# and then converted into a list of integers using map() function and then make a tuple using tuple().
tp1 = tuple(map(int, user_input.split()))

# Prompt the user to enter an integer they want to search for in the tuple.
num = int(input('Enter integer you want to search: '))

# Initialize a variable to count the occurrences of the specified integer.
occ = 0

# Iterate through each integer in the tuple.
for i in tp1:
    
    # Check if the element i is equal to the integer num specified by the user.
    if(i == num):

        # The counter occ is incremented by 1
        occ += 1

# Print the frequency of the specified integer in the tuple.
print('Frequency of', num, ': ', occ)
