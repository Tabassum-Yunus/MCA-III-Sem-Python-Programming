'''     Write a Python program to find the index of an item in a tuple.     '''


l1 = input('Enter the list of integers separated by space: ')
tup = tuple(map(int, l1.split()))

j = k = 0
inp = int(input('Enter an int to find its index: '))
print('Index of',inp,': ', end=' ')
for i in tup:
    if(i == inp):
        print(j, end=' ')
        k += 1
    j += 1

if(k==0):
    print('Not found in tuple')