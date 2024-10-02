'''     Consider two files that contain information about Employees and Departments in the following parameters: 
        Employee (Name, EId, Salary, DID), Department (DID, DName, DLocation). Write a Python program to find 
        the average salary of each department.      '''


'''                                             APPROACH 1                                      '''

# Open the Department and Employee files for reading
dept_file = open('D:\MyVScodeProgs\Programs\Python\Week 7\Department.txt', 'r')
emp_file = open('D:\MyVScodeProgs\Programs\Python\Week 7\Employee.txt', 'r')

# Create a dictionary to store department IDs as keys and a list of employee salaries for each department
dept_employee = dict()

# Reading the Department file
for line in dept_file:
    line = line.split()  # Split the line by whitespace to get individual data items
    deptID = line[0]  # Extract the department ID (DID) from the first item
    dept_employee[deptID] = []  # Initialize an empty list for storing employee salaries for each department

# Reading the Employee file
for line in emp_file:
    line = line.split()  # Split the line to extract employee data
    emp_sal = line[-2]  # Extract the employee's salary (second last item)
    deptID = line[-1]  # Extract the department ID (last item) to associate the employee with the department
    dept_employee[deptID].append(float(emp_sal))  # Append the employee's salary to the respective department's list

# Calculate and print the average salary for each department
for dept, emp_salaries in dept_employee.items():
    if len(emp_salaries) > 0:  # If there are employees in the department
        avg_salary = sum(emp_salaries) / len(emp_salaries)  # Calculate average salary
        print('Department id: ', dept, ',\tAverage Salary: ', avg_salary)
    else:  # If no employees in the department
        print('Department id: ', dept, ',\tNo employee')

# Close the files to release resources
dept_file.close()
emp_file.close()



'''                                             APPROACH 2                                      '''
'''
# Open the Department and Employee files for reading
dept_file = open('D:\MyVScodeProgs\Programs\Python\Week 7\Department.txt', 'r')
emp_file = open('D:\MyVScodeProgs\Programs\Python\Week 7\Employee.txt', 'r')

# Initialize two dictionaries:
# 1. dept_no_emp will store the number of employees in each department.
# 2. dept_sal will store the total salary for each department.
dept_no_emp = {}
dept_sal = {}

# Reading the Department file
for line in dept_file:
    line = line.split()  # Split the line to get department details
    deptID = line[0]  # Get the Department ID (DID)
    dept_no_emp[deptID] = 0  # Initialize the number of employees for each department to 0

# Reading the Employee file
for line in emp_file:
    line = line.split()  # Split the line to get employee details
    deptID = line[-1]  # Get the Department ID the employee belongs to (last item in the line)
    salary = float(line[-2])  # Get the employee's salary (second last item)
    
    # Update total salary for the department
    dept_sal[deptID] = dept_sal.get(deptID, 0) + salary  # If the deptID is not in dept_sal, it will initialize to 0
    
    # Update the number of employees in the department
    dept_no_emp[deptID] = dept_no_emp.get(deptID, 0) + 1  # If the deptID is not in dept_no_emp, it will initialize to 0

# Initialize a new dictionary to store the average salary for each department
dept_AvgSal = {}

# Calculating the average salary for each department without a nested loop
# Loop through each department ID in the dept_no_emp dictionary (which stores the number of employees)
for deptID in dept_no_emp:
    
    # Check if the department has employees (number of employees > 0)
    if dept_no_emp[deptID] > 0:
        # Calculate the average salary by dividing the total salary (from dept_sal)
        # by the number of employees (from dept_no_emp) for that department
        dept_AvgSal[deptID] = dept_sal[deptID] / dept_no_emp[deptID]
    else:
        # If no employees are present in the department, set the average salary to 0
        dept_AvgSal[deptID] = 0

# Printing the average salary for each department
for dept, sal in dept_AvgSal.items():
    if sal > 0:  # If there's a positive salary, print the average
        print('Department id: ', dept, ',\tAverage Salary: ', sal)
    else:  # If no employees in the department, print a message
        print('Department id: ', dept, ',\tNo employee')

# Close the files after reading
dept_file.close()
emp_file.close()

'''
