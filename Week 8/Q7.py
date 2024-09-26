'''     Write a Python program to create a list of user's supplied distinct integers having even number
        of elements. The program further creates two lists of equal lengths based on the original list,
        where first list is having all elements less than elements of second list. Display both the lists.      '''

import copy as c
l = list(map(int, input('Enter list of integers: ').split()))
a = c.deepcopy(l)
a = sorted(a)
first_list = []
second_list = []
mid = a[len(a)//2]
for i in l:
    if(i <= mid):
        first_list.append(i)
    else:
        second_list.append(i)
print('First list: ',first_list)
print('Second list: ',second_list)
        