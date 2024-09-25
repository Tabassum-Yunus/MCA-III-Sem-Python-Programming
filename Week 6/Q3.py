'''     Write a Python program having a void function that receives a 4-digit number
        and calculates the sum of squares of first 2 digits' number and last two digits'
        number, e.g. if 1233 is passed as argument then function should calculate 12^2 + 33^2.    '''


def square(num):
    
    # Check if the number has less than four digits. If yes, return
    if(no <= 999):  
        print('Number is less than four digits')
        return

    # Copy the original number to n for digit counting
    n = num
    no_of_digits = 0
    
    # Loop to count the number of digits in the number
    while(n != 0):
        no_of_digits += 1
        n //= 10

    # Print the original number
    print('Original number: ', num)
    
    # Extract the first two digits by dividing the number by 10^(no_of_digits-2)
    first_two_digits = num // (10 ** (no_of_digits - 2))  
    print('First two digits: ', first_two_digits)
    
    # Extract the last two digits using modulo 100
    last_two_digits = num % 100  
    print('Last two digits: ', last_two_digits)
    
    # Calculate the sum of the squares of the first two and last two digits
    result = (first_two_digits ** 2) + (last_two_digits ** 2)
    
    # Print the result
    print('Sum of square of first & last two digits: ', result)


# Take input from the user
no = int(input('Enter a 4 or more digits integer: '))

# Call the square function to compute the sum of squares
square(no)
