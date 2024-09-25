'''     Write a program to compute the value of the following algebraic expression- (1+(x/y)+x^y) / (2+(y/x)+y^x)  '''

# Taking input from the user for the values of x and y, converting them to floats
x = float(input('Enter value of x: '))
y = float(input('Enter value of y: '))

# Computing the algebraic expression: (1 + (x / y) + x^y) / (2 + (y / x) + y^x)
expression = (1 + (x / y) + (x ** y)) / (2 + (y / x) + (y ** x))

# Printing the result of the evaluated expression
print('Value of expression is: ', expression)
