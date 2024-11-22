'''     Write programs in python to sort a List according to the length of the elements.    '''

l = input('Enter a list of strings separated by space: ')
list1 = list(l.split())
print(list1)
for i in range(0, len(list1)):
    for j in range(i+1, len(list1)-1):
        if(list1[j] > list1[j+1]):
            list1[i], list1[j] = list1[j], list1[i]

print(list1)


