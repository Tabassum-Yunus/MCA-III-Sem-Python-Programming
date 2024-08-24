'''     Write a program to create function cal_sum_sub() such that it can accept two
        variables and calculate addition and subtraction. Also, it must return both
        addition and subtraction in a single return call.       '''


# Funtion to calculate the addition and subtraction of two numbers.
def cal_sum_sub(a, b):              # a, b are thr parameters

    # Calculate addition
    add = a + b
    # Calculate subtraction
    sub = a - b
    
    # Return both results
    return add, sub

# Prompt the user to enter the first number and convert it into integer
a = int(input("Enter first number: ")) 

# Prompt the user to enter the second number and convert it into integer
b = int(input("Enter second number: "))  

# Call the function with user inputs and store the results
sum, diff = cal_sum_sub(a, b)

# Display the results
print("Addition of",a,"and",b,": ",sum)
print("Subtraction of",a,"and",b,": ",diff)
