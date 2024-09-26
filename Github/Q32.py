'''     Write a Python program to remove an empty tuple(s) from a list of tuples.   '''

l1 = input('Enter a list separated by space: ')
a = list( l1.split())
print(a)
for i in a:
    try:
        x = int(i)
    except:
        a.remove(i)
print(a)