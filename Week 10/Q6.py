'''     Consider two files that contain information about Employees and Departments in the following parameters: 
        Employee (Name, EId, Salary, DID), Department (DID, DName, DLocation). Write a Python program to merge 
        the content of both the file in following format.: Emp_Dep(Ename, Eid, Esalary, EDID, DName,Dlocation) 
        (Note: Merging should follow the condition-DID of Employee file should be equal to Department ID of 
        department file)     '''


emp_file = open('D:\MyVScodeProgs\Programs\Python\Week 10\Employee.txt','r')
dept_file = open('D:\MyVScodeProgs\Programs\Python\Week 10\Department.txt','r')
emp_dept_file = open('D:\MyVScodeProgs\Programs\Python\Week 10\Emp_Dept.txt','w')

emp_content = emp_file.readlines()
dept_content = dept_file.readlines()
# print(dept_content)

for line in emp_content:
    emp = line.strip()
    empp = emp.split()
    # print(emp)
    emp_dept = empp[-1]
    for line1 in dept_content:
        dept = line1.strip()
        deptt = dept.split(',')
        # print(dept)
        dept_no = deptt[0]        
        if(emp_dept == dept_no):
            emp_dept_file.write(emp+','+deptt[1]+','+deptt[2]+'\n')

emp_file.close()
dept_file.close()
emp_dept_file.close()



