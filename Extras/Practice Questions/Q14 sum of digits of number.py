'''     Write a Python function to calculate the sum of digits of a given integer.      '''

num = int(input('Enter an integer: '))
sum = 0
while(num != 0):
    rem = num%10
    sum += rem
    num //= 10
print(sum)