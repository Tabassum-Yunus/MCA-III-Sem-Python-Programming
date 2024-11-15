'''     Write programs in python for the following:
        Read a list and transfer even and odd integers into Two Different Lists.    '''

l = input('Enter a list of integers separated by space: ')
list1 = list(map(int, l.split()))
l_even = []
l_odd = []
for i in list1:
    if(i%2 == 0):
        l_even.append(i)
    else:
        l_odd.append(i)
print(l_even)
print(l_odd)