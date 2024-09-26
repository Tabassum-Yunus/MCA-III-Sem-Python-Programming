'''     Write a program to find prime numbers between two numbers.      '''

import math as mt
print('Enter range to find prime numbers')
start = int(input('Start: '))
end = int(input('End: '))

print('Prime numbers: ',end='')
for i in range(start, end+1):
    for j in range(2, int(mt.sqrt(i)+1)):
        if(i%j == 0):
            break
    else:
        print(i,end=' ')
