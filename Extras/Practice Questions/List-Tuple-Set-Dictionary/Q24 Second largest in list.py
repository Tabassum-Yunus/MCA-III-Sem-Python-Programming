'''     Write programs in python to find the second largest number in a List and all its index.     '''

l = input('Enter a list of integers separated by space: ')
list1 = list(map(int, l.split()))

list1 = sorted(list1)
print(list1)

max = list1[len(list1)-1]
s_max = list1[0]
for i in range(len(list1)-1 , 0, -1):
    if(i>s_max and i!=max):
        s_max = i
        break
print('Max: ',max)
print('S_max: ',s_max)

