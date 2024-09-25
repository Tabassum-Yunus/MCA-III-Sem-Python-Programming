'''     Given a list containing strings and integers. Write a program to create two separate 
        lists consisting of strings and integers respectively.     '''

l = input('Enter combination of numbers & strings separated by space: ')
list = l.split()
l_string = []
l_integers = []
for i in list:
    try:
        l_integers.append(int(i))
    except:
        l_string.append(i)

print(l_integers)
print(l_string)