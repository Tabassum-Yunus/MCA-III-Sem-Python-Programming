'''     Consider two files having some lines of statements. Write a Python program to swap content 
        present at middle line of first file with the content of last line of the second file. 
        (Note: First file contains odd numbers of lines of statement)     '''

# Open the two files in read mode
file1 = open('D:\MyVScodeProgs\Programs\Python\Week 7\File1_W7Q6.txt', 'r')
file2 = open('D:\MyVScodeProgs\Programs\Python\Week 7\File2_W7Q6.txt', 'r')

# Read all lines from both files and store them in lists
file1_lines = file1.readlines()
file2_lines = file2.readlines()

# Display the content before swapping
print('BEFORE SWAPPING')
print('Content of file 1: ', file1_lines)
print('Content of file 2: ', file2_lines)

# Close the files as the reading operation is complete
file1.close()
file2.close()

# Re-open the files in write mode to apply changes after swapping
file1 = open('D:\MyVScodeProgs\Programs\Python\Week 7\File1_W7Q6.txt', 'w')
file2 = open('D:\MyVScodeProgs\Programs\Python\Week 7\File2_W7Q6.txt', 'w')

# Swap the content of the middle line of file1 with the last line of file2
file1_lines[len(file1_lines)//2], file2_lines[len(file2_lines)-1] = file2_lines[len(file2_lines)-1], file1_lines[len(file1_lines)//2]

# Display the content after swapping
print('AFTER SWAPPING')
print('Content of file 1: ', file1_lines)
print('Content of file 2: ', file2_lines)

# Write the modified content back into the files
file1.writelines(file1_lines)
file2.writelines(file2_lines)

# Close the files after writing is done
file1.close()
file2.close()
