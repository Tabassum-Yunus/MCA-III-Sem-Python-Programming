'''     Consider two text files with some content. Copy the contents of them in third file such that 
line 1 of third file will have line 1 of first file, line 2 of third file will have line 1 of second file,
line 3 of third file will have line 2 of first file, line 4 of third file will have line 2 of second file
and so on   '''

# Open the input files for reading
fh1 = open('D:\\MyVScodeProgs\\Programs\\Python\\Sessional\\FileA.txt', 'r')  # Open FileA.txt
fh2 = open('D:\\MyVScodeProgs\\Programs\\Python\\Sessional\\FileB.txt', 'r')  # Open FileB.txt

# Open the output file for writing
fh3 = open('D:\\MyVScodeProgs\\Programs\\Python\\Sessional\\FileC.txt', 'w')  # Create FileC.txt

# Infinite loop for reading lines from both files
while True:  

    fileA_line = fh1.readline()  # Read a line from FileA
    fileB_line = fh2.readline()  # Read a line from FileB
    
    # Write the lines read to FileC
    fh3.write(fileA_line)  # Write line from FileA
    fh3.write(fileB_line)  # Write line from FileB
    
    # Check if both files have reached the end
    if fileA_line == '' and fileB_line == '':
        break  # Exit the loop if both files are done

    # If FileA is done but FileB still has lines, write the remaining lines from FileB
    if fileA_line == '' and fileB_line != '':
        while fileB_line:  # While there are still lines in FileB
            fh3.write(fileB_line)  # Write the line to FileC
            fileB_line = fh2.readline()  # Read the next line from FileB
        break  # Exit the loop after writing all lines from FileB

    # If FileB is done but FileA still has lines, write the remaining lines from FileA
    if fileB_line == '' and fileA_line != '':
        while fileA_line:  # While there are still lines in FileA
            fh3.write(fileA_line)  # Write the line to FileC
            fileA_line = fh1.readline()  # Read the next line from FileA
        break  # Exit the loop after writing all lines from FileA

# Close all files after operations are complete
fh1.close()  # Close FileA
fh2.close()  # Close FileB
fh3.close()  # Close FileC
