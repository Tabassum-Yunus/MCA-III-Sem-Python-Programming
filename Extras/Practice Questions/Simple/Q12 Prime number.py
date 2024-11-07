'''     Write a program to check whether the integer is prime.      '''

import math as mt
no = int(input('Enter a number: '))
for i in range(2, int(mt.sqrt(no)+1) ):
    if(no%i == 0):
        print(no, 'is not a prime.')
        break
else:
    print(no, 'is priime')