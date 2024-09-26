'''     Write a program to get roll numbers, names and marks of the students of a class
        (get from user) and store these details in a file called “Marks.data”.'''

fh = open('File_W6Q5.txt', 'w+')
fh.write('NAME          ROLL NO         MARKS')
print('Enter name, roll no and marks of strudents')
while(True):
    name = input('Name: ')
    roll_no = input('Roll No: ')
    marks = list(input('Mark(s): ').split())
    marks = ', '.join(map(str, marks))
    fh.write(name,'         ', roll_no,'        ', marks)
    inp = input('Want to Quit? Y/N: ')
    if(inp == 'y' or inp == 'Y'):
        break
    
fh.close()
