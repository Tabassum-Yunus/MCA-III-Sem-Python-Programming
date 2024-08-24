
'''     Write a program to display all prime numbers within a range     '''


# Import math library 
import math

# Print the supplied string
print("Enter range to generate prime numbers")

# Prompt the user to enter the starting value of range and convert it into integer
start = int(input("Start: "))       

# Prompt the user to enter the end value of range  and convert it into integer
end = int(input("End: "))

# Print the the range of prime numbers without moving to a next line
print("Prime numbers between", start, "and", end, ":", end=" ")

# Loop through each number in the specified range
for i in range(start, end + 1):
        
        # Assume the number is prime initially
        is_prime = True

        # Check divisibility of the number by any integer from 2 to the square root of the number
        for j in range(2, int(math.sqrt(i)) + 1):
            
            # Check if the number is divisible by any j
            if i % j == 0:

                # Set the flag to False, indicating it's not prime
                is_prime = False  

                # Exit the inner loop as a divisor has been found
                break  
    
        # If no divisors were found and check is_prime is still True
        if is_prime:

            # Print the found prime number on the same line
            print(i, end=" ")  

