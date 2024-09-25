'''     Write a python program to count frequency of each character in a line of text.  '''

st = input('Enter a string: ')

d = dict()
for i in st:
    if(ord(i) != 32):
        d[i] = d.get(i,0)+1
print(d)