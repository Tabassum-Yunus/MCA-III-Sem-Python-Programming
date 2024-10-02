'''     Write a program to get roll numbers, names and marks of the students of a class
        (get from user) and store these details in a file.      '''

# Open the file in write mode to store student data
file = open('D:\MyVScodeProgs\Programs\Python\Week 6\File_W6Q5.txt', 'w')

# Prompt the user to enter name, roll number, and marks of students
print('Enter name, roll no and marks of students')

# Write the header for the file (column names)
file.write('NAME \t ROLL NO. \t MARKS\n')

# Start an infinite loop to keep accepting student data until the user decides to quit
while(True):
    # Input student name
    name = input('Name: ')
    
    # Input student roll number
    roll_no = input('Roll No: ')
    
    # Input marks (multiple marks entered as a space-separated string and converted into a list)
    marks = list(input('Mark(s): ').split())
    
    # Join the list of marks into a comma-separated string
    marks = ', '.join(map(str, marks))
    
    # Write the student data (name, roll number, and marks) into the file in a formatted manner
    file.write(name + ' \t ' + roll_no + ' \t\t' + marks + '\n')
    
    # Ask the user if they want to quit the input process
    inp = input('Want to Quit? Y/N: ')
    
    # Break the loop if the user enters 'y' or 'Y', otherwise continue
    if inp == 'y' or inp == 'Y':
        break

# Close the file after writing is complete
file.close()

