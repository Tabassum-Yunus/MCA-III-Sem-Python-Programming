'''   Write a program in python to count number of sentences, no. of words and the word having maximum instance.  '''

l1 = input('Enter a string: ')
list1 = list( l1.split('.'))
print('No. of sentences: ', len(list1))
list2 = list( l1.split())
print('No. of words: ', len(list2))

d = dict()
for i in list2:
    d[i] = d.get(i,0) + 1
v_list = d.values()
m = max(v_list)
for i,j in d.items():
    if(j == m):
        print('Word: ',i)
        print('Freq: ', j)
        