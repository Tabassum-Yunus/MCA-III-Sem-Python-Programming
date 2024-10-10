'''     Read a List of Words and Return the Length of the Longest One   '''


l1 = input('Enter the list of strings separated by space: ')
list1 = list(l1.split())

m = max(list1)
# print(m,'  ',len(m))
for i in list1:
    if(len(i) == len(m)):
        print(i,end=' ')