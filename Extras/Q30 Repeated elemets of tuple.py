'''     Write a Python program to find the repeated items of a tuple.   '''

l1 = input('Enter the list of integers separated by space: ')
tup = tuple(map(int, l1.split()))
d = dict()
for i in tup:
    d[i] = d.get(i,0)+1
print(d)

for i,j in d.items():
    if(j > 1):
        print(i,' ',end=' ')