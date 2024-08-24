
'''     Write a program to use the loop to find the factorial of a given number.     '''


# Prompt the user to enter a number and convert it into integer
num = int(input("Enter a no.: "))

# Initialize a variable to hold the factorial
fac = 1

# Loop through 1 to num to calculate factorial of number
for i in range(1,num+1):
    # Multiply factorial with the current value of i
    fac *= i  

# Print the fatorial of the number
print("Factorial of",num,":",fac)