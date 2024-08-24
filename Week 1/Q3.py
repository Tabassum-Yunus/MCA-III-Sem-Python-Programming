'''     Write a program to Iterate the supplied list of 20 numbers by the user and print
        only those numbers which are divisible by 5.    '''


# Initialize an empty list to store numbers divisible by 5
list = []

# Loop 20 times to get 20 numbers from user 
for i in range(1,21):
    # Prompt the user to enter a number and convert it into integer
    x = int(input("Enter an integer: "))

    # Check if the entered number is divisible by 5
    if(x%5 == 0):
        # If the number is divisible by 5, add it to the list
        list.append(x)

# Print the list of numbers that are divisible by 5
print("Numbers divible by 5: ", list)