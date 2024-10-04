'''     A file contains information about employees with the following parameters: Name, Id, Salary, Dname. 
        Write a Python program to write one more column HRA (House rent allowances) to this file, 
        where HRA= 18% of salary
        Eg: Suppose the existing file is as follows, where you need to add HRA column:
        Name,id,salary,Dname
        Amar,101,20000,Sales 
        Ammar,102,22000,Marketing 
        Rahil,103,18000,Sales
        -------      '''



'''                                          APPROACH 1                                      '''

# Open the file in read+write mode
file1 = open('D:\MyVScodeProgs\Programs\Python\Week 9\HRA.txt', 'r+')

# Initialize an empty list to store the modified lines with the new HRA column
modified_lines = []  

# Loop through each line in the file
for line in file1:
    # Split each line by commas to separate the employee details into a list
    splitted_line = line.split(',')
    
    # Extract the salary from the third element of the list (index 2) and convert it to a float
    salary = float(splitted_line[2])
    
    # Calculate the HRA as 18% of the salary
    hra = 0.18 * salary
    
    # Add the HRA value to the end of the line, then strip any extra whitespace or newline characters
    # Reconstruct the line by appending the HRA, followed by a newline character
    modified_lines.append(line.strip() + ', ' + str(hra) + '\n')

# Move the file pointer back to the beginning of the file
file1.seek(0)

# Write the modified lines back to the file (overwriting the old content)
file1.writelines(modified_lines)

# Close the file
file1.close()




'''                                          APPROACH 2                                      '''

# file1 = open('D:\MyVScodeProgs\Programs\Python\Week 9\HRA.txt', 'r+')
# lines = file1.readlines()  # Read all lines
# new_lines = []
# for line in lines:
#     print(line)
#     splitted_line = line.split(',')
#     salary = float(splitted_line[2])
#     hra = 0.18 * salary
#     new_lines.append(line.strip() + ', ' + str(hra) + '\n')

# file1.seek(0)
# file1.writelines(new_lines)
# file1.close()


'''                                          APPROACH 3                                      '''

# file1 = open('D:\MyVScodeProgs\Programs\Python\Week 9\HRA.txt', 'r+')

# for line in file1:
#     splitted_line = line.split(',')
#     lenn = len(splitted_line)
#     salary = float(splitted_line[2])
#     hra = 0.18 * salary
#     file1.seek(0,0)
#     file1.write(line.strip()+', '+ str(hra) + '\n')
# file1.close()




