'''     Write a Python program having a void function that receives a 4-digit number
        and calculates the sum of squares of first 2 digits' number and last two digits'
        number, e.g. if 1233 is passed as argument then function should calculate 12^2 + 33^2.    '''


def square(num):

    n = num
    no_of_digits = 0
    while(n != 0):
        no_of_digits += 1
        n //= 10

    # Extract the first two digits
    first_two_digits = num // (100)  # Divide by 100 to get the first two digits
    
    # Extract the last two digits
    last_two_digits = num % 100  # Modulo by 100 to get the last two digits
    
    # Calculate the sum of squares
    result = (first_two_digits ** 2) + (last_two_digits ** 2)
   
    print('Sum of square of fisrt & last two digits: ',result)


no = int(input('Enter a 4 or more digits integer: '))
print('Original number: ', end='')
square(no)
