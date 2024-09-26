'''  Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number.'''

l1 = input('Enter a frist list of integers separated by space: ')
list1 = list(map(int, l1.split()))
list2 = []
for i in list1:
    t = (i, i**2)
    list2.append(t)
print(list1)
print(list2)