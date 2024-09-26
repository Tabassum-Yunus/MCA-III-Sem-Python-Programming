'''     Create your own class prime to return all primes between two given numbers.     '''

import math as mt

class Prime:
    def __init__(self, st, end):
        self.st = st
        self.end = end
        for i in range(st,end+1):
            for j in range(2, int(mt.sqrt(i))+1):
                if(i%j == 0):
                    break
            else:
                print(i, end=' ')
        
print('Prime numbers within given range: ', end='')
p = Prime(5, 20)
