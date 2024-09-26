'''     Write a program to read the values of two points on x-y plane and find out the distance 
        between two points. Use math functions (sqrt, pow). '''


import math as mt
print('Enter two points in x-y plane: ')
x1 = float(input('x1: '))
y1 = float(input('y1: '))
x2 = float(input('x2: '))
y2 = float(input('y2: '))

distance = mt.sqrt( mt.pow(x1-y1,2) + mt.pow(x2-y2,2) )
print(distance)

