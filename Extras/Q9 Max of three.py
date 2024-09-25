'''     Write a program to find the maximum of three numbers.   '''

print('Enter three numbers')
x,y,z = float(input().split())

max = x if(x>y and x>z) else y if(y>x and y>z) else z
print(max)