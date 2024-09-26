'''     Write a python program to find character having maximum count in a line of text.    '''

st = input('Enter a string: ')

d = dict()
for i in st:
    if(ord(i) != 32):
        d[i] = d.get(i,0)+1
l = d.values()
m = max(l)
for i,j in d.items():
    if(j == m):
        print('Count: ', m)
        print('Word(s): ', i)