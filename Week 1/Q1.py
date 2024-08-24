'''     Write a program to find product of two user supplied integers and if the product
        is equal to or lower than 5000 then return sum of the two numbers.'''


# Prompt the user to enter the first number and convert it into integer
a = int(input("Enter first number: "))      

# Prompt the user to enter the second number and convert it into integer
b = int(input("Enter second number: "))        

 # Calulate product of the entered numbers
prod = a*b                         

# Check if product is less than or equal to 5000
if( prod <= 5000 ):
    # if the condition met, print sum of entered numbers
    print("Sum of ", a, " and ", b,": ", (a+b))
else:
    # if the condition isn't met, print the product of entered numbers
    print("Product is greater than 5000")