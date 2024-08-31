
'''     Write a program to generate 6 digit random secure OTP.      '''

# Import random module and aliased as r for easier usage in the code.
import random as r

# Generate a random 6-digit number between 100,000 and 999,999 using the randrange() function.
password = r.randrange(100000, 999999)

# Print the randomly generated password.
print(password)
