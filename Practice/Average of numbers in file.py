'''     Find the average of numbers present in file. File may contain any data type     '''

# Open the file for reading
fh1 = open('D:\\MyVScodeProgs\\Programs\\Python\\Sessional\\FileAvg.txt', 'r')

# Initialize variables to store the count of numbers and their sum
count = 0  
sum = 0  

# Print header for numbers being read
print('Numbers: ', end='')

# Loop through each line in the file
while True:
    line = fh1.readline()  # Read one line from the file
    
    # If the line is empty (end of file), break the loop
    if line == '':
        break
    
    # Split the line into words (numbers in string form)
    words = line.split()
    
    # Iterate through each word in the line
    for i in words:
        try:
            # Try to convert the word to a float
            sum += float(i)  # Add the number to the sum
            print(i, end=' ')  # Print the valid number
            count += 1  # Increment the count of numbers
        except:
            # If a word is not a valid number, ignore it
            pass

# Calculate and print the average of the numbers
print(sum / count)  # Print the average of the numbers

