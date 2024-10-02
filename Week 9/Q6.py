'''     A file contains information about programs and courses in the following format: Program,course. 
        Write a Python program to find the number of courses against each program.
        Eg:
        Program,Course
        MCA,Database 
        MCA,Java 
        M.Sc,Data Structure
        B.Sc, Python
        ------
        
        The output should be: MCA-2, M.Sc-01, B.Sc-01       '''


# Open the file in read mode.
file1 = open('D:\MyVScodeProgs\Programs\Python\Week 9\Programs-Courses.txt', 'r')

# Initialize an empty dictionary to store programs and their respective course counts.
prog_courses = {}

# Iterate through each line in the file.
for line in file1:
    # Split the line by the comma to separate the program from the course.
    line = line.split(',')
    
    # Extract the program name, which is the first element.
    program = line[0]
    
    # Extract the course name. It's the last element after the comma.
    course = line[-1]
    
    # Update the program's course count in the dictionary. If the program is not already in the dictionary, 
    # it initializes the count with 0 and then increments by 1.
    prog_courses[program] = prog_courses.get(program, 0) + 1

# Iterate through the dictionary to print the program name and its course count.
for program, no_courses in prog_courses.items(): 
    # Print the program name along with the number of courses.
    print('Program:', program, ',\t No. of Courses:', no_courses)
#     print(program,'-', no_courses,',',end=' ')