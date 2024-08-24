
'''     Write a program to calculate the cube of all numbers from 1 to a given number.  '''

# Prompt the user to enter the upper limit number and convert it to an integer
num = int(input("Enter the number: "))

# Iterate through all numbers from 1 to the upper limit
for num in range(1, num + 1):
    # Calculate the cube of the current number
    cube = num ** 3
    # Print the number and its cube
    print("The cube of ", num, " is ", cube)

