'''     Write a program to get roll numbers, names and marks of the students of a class
        (get from user) and store these details in a file.      '''

fh = open('D:\MyVScodeProgs\Programs\Python\Week 6\File_W6Q5.txt', 'w')
print('Enter name, roll no and marks of strudents')

fh.write('NAME \t ROLL NO. \t MARKS\n')
while(True):
    name = input('Name: ')
    roll_no = input('Roll No: ')
    marks = list(input('Mark(s): ').split())
    marks = ', '.join(map(str, marks))
    fh.write(name+' \t '+roll_no+' \t\t'+marks+'\n')
    inp = input('Want to Quit? Y/N: ')
    if(inp == 'y' or inp == 'Y'):
        break
fh.close()
