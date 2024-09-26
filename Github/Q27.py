'''     Write programs in python to remove the duplicate items from a List.     '''

l = input('Enter a list of strings separated by space: ')
list1 = list(l.split())
print(list1)
l1 = len(list1)
for i in range(0, l1-1):
    for j in range(i+1, l1-1):
        if(list1[i] == list1[j]):
            list1.remove(list1[j])
            l1 -= 1

print(list1)