'''     Write programs in python to find element occurring odd number of times in a list.   '''

l1 = input('Enter the list of integers separated by space: ')
list1 = list(map(int, l1.split()))
d = dict()

for i in list1:
    d[i] = d.get(i,0)+1
print(d)

for i,j in d.items():
    if(j%2 != 0):
        print(i,' ',end=' ')