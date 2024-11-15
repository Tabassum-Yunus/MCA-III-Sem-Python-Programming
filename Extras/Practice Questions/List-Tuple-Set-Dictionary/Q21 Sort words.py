'''     Write Python Program to Sort Words in Alphabetic Order.     '''

l = ['sdb', 'qwe', 'ads']
l = sorted(l)
sorted_string = ' '.join(l)
print(sorted_string)


''' BUBBLE SORT '''
a = [2,5,3,8,6]
print(a)
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if(a[j]>a[j+1]):
            a[j], a[j+1] = a[j+1], a[j]
print(a)