
'''     Write a program to print the following pattern using the for loop:
                    5 4 3 2 1 
                    4 3 2 1
                    3 2 1
                    2 1
                    1                                   '''



# Prompt the user to input the number of rows for the pattern
rows = int(input("Enter no. of rows: "))

# Outer loop: Controls the number of rows, starting from 'rows' down to 1
for i in range(rows, 0, -1):

    # Inner loop: Controls the number within each row, starting from 'i' down to 1
    for j in range(i, 0, -1):

        # Print the current value of 'j' followed by a space, keeping the output on the same line
        print(j, end=" ")

    # Move to the next line after each row is printed
    print()


