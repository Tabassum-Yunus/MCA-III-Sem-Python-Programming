'''     5.	Write a program in python to find alphabet/s having maximum number of instances in a given file.    '''

# Open the file 'File_W9Q5.txt' in read and write mode (r+)
fh = open('D:\MyVScodeProgs\Programs\Python\Week 9\File_W9Q5.txt', 'r+')

# Initialize an empty dictionary to store the count of each character (including all alphabets and other characters)
d = dict()

# Start an infinite loop to read the file line by line
while(True):
    # Read one line from the file
    line = fh.readline()
    
    # Convert the line to lowercase to ensure case-insensitive counting
    line = line.lower()
    
    # Iterate through each character in the line
    for i in line:
        # Skip spaces (don't count them)
        if(i != ' '):
            # Add the character to the dictionary and increment its count
            d[i] = d.get(i, 0) + 1
    
    # If the line is empty (i.e., end of file), break the loop
    if(line == ''):
        break

# Close the file after reading its contents
fh.close()

# Initialize a variable to keep track of the maximum count of any alphabet
m = 0
key = []  # List to store all alphabets with the maximum instances

# Iterate through the dictionary to find the alphabets with the maximum count
for i, j in d.items():
    # Check if the current character is an alphabet (ignores numbers and special characters)
    if i.isalpha():
        # If the count of the current alphabet is greater than the current max `m`
        if(j > m):
            m = j
            key = [i]  # Reset the list with the new maximum character
        elif(j == m):
            key.append(i)  # Append to the list if it matches the current maximum

# Print the alphabets with the maximum instances
print('Alphabets with maximum instances: ', set(key))  # Use set to eliminate duplicates
