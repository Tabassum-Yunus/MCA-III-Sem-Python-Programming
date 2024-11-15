'''     Write programs in python WAP to merge Two Lists and Sort it.    '''

l1 = input('Enter a frist list of integers separated by space: ')
list1 = list(map(int, l1.split()))
l2 = input('Enter a second list of integers separated by space: ')
list2 = list(map(int, l2.split()))

list3 =list1+list2
print(sorted(list3))