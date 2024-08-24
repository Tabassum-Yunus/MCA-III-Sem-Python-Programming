'''     Write a program to print the following start pattern using the for loop:
                         *
                         * *
                         * * *
                         * * * *
                         * * *
                         * *
                         *               '''



# Prompt the user to input the number of rows for the pattern
rows = int(input("Enter no. of rows: "))

# First part of the pattern: Increasing sequence of '*'

# Loop to control the number of rows, starting from 1 up to 'rows'
for i in range(1, rows+1):

    # Print '*' repeated 'i' times on the same line
    print('*'*i)

# Second part of the pattern: Decreasing sequence of '*'

# Loop to control the number of rows, starting from 'rows-1' down to 1
for i in range(rows-1, 0, -1):

    # Print '*' repeated 'i' times on the same line
    print('*'*i)





'''
# Prompt the user to input the number of rows for the pattern
rows = int(input("Enter no. of rows: "))

# First part of the pattern: Increasing sequence of '*'

# Outer loop: Controls the number of rows, starting from 1 up to 'rows'
for i in range(1, rows+1):

    # Inner loop: Controls the number of * within each row, starting from 1 up to 'i'
    for j in range(1, i+1):

        # Print the current value of 'j' followed by a space, keeping the output on the same line
        print('*', end=" ")

    # Move to the next line after each row is printed
    print()
    
# Second part of the pattern: Decreasing sequence of '*'

# Outer loop: Controls the number of rows, starting from 'rows-1' down to 1
for i in range(rows-1, 0, -1):

    # Inner loop: Controls the number within each row, starting from 'i' down to 1
    for j in range(i, 0, -1):

        # Print the current value of 'j' followed by a space, keeping the output on the same line
        print('*', end=" ")

    # Move to the next line after each row is printed
    print()
'''