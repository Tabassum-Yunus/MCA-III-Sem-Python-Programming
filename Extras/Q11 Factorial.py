'''     Write a program to compute the factorial of an integer.     '''

x = int(input('Enter an integer: '))
fact =1
for i in range(2,x+1):
    fact *= i
print('Factorial of ',x,': ',fact)