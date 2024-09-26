'''     Write a program in python to find vowels having maximum number of instances in a given file.    '''


# Open the file 'File_W8Q6.txt' in read mode (r)
fh = open('File_W8Q6.txt', 'r+')

# Initialize an empty dictionary to store the count of vowels
d = dict()

# Start an infinite loop to read the file line by line
while(True):
    # Read one line from the file
    line = fh.readline()
    
    # Convert the line to lowercase to handle both uppercase and lowercase vowels
    line = line.lower()
    
    # Iterate through each character in the line
    for i in line:
        # Ignore spaces and process only other characters
        if(i != ' '):
            # Check if the character is a vowel (a, e, i, o, u)
            if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
                # If it's a vowel, increment its count in the dictionary
                # If the vowel is not in the dictionary, use d.get(i, 0) to return 0 and then add 1
                d[i] = d.get(i, 0) + 1
    
    # If the line is empty, break the loop (end of file reached)
    if(line == ''):
        break

# Print the dictionary containing vowel counts
print(d)

# Close the file
fh.close()

# Initialize variable `m` to keep track of the maximum count of vowels
m = 0

# Loop through the dictionary to find the vowel with the maximum instances
for i, j in d.items():
    # If the count of the current vowel is greater than `m`, update `m` and store the vowel as `key`
    if(j > m):
        m = j
        key = i

# Print the vowel with the maximum instances
print('Vowel with maximum instances: ', key)
