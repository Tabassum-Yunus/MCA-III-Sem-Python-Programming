'''     Write a Python program to create a Python dictionary (the dictionary type).
        Add three names and their phone numbers in the dictionary. The names should
        act as a keys and phones as their values. Then ask the user a name and print its
        corresponding phone number.     '''


# Initialize an empty dictionary to store names and phone numbers
d = dict()

# Prompt the user to enter three names and their phone numbers
print('Enter three names and their phone numbers: ')

# Loop for three inputs
for i in range(3):
    
    # Take the name as input from the user
    name = input()
    
    # Take the corresponding phone number as input
    ph_no = input()
    
    # Store the name and phone number in the dictionary
    d[name] = ph_no

# Print the entire dictionary to display all entered names and phone numbers
print(d)

# Prompt the user to enter the name they want to search for
n = input('Enter a name whose no. you want to search: ')

# Try to search for the phone number of the entered name
try:
    # If the name exists, print the corresponding phone number
    print('Phone no. of "', n, '" is ', d[n])
    
# If the name is not found, handle the exception and print a message
except:
    print('User does not exist')

