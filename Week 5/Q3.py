'''     3. Write a program to generate a random Password which meets the following conditions
            a. Password length must be 10 characters long.
            b. It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.    '''


# Import the random module for generating random characters
import random  

# Generate one random special symbol
symbol = [chr(random.randrange(33, 47))]  # ASCII values for special symbols from '!' (33) to '/' (46)

# Generate one random digit
digit = [chr(random.randrange(48, 58))]  # ASCII values for digits from '0' (48) to '9' (57)

upper = []  # List to store uppercase letters
lower = []  # List to store lowercase letters

# Generate two random uppercase letters
for i in range(2):
    upper.append(chr(random.randrange(65, 91)))  # ASCII values for uppercase letters from 'A' (65) to 'Z' (90)

# Generate six random lowercase letters
for i in range(6):
    lower.append(chr(random.randrange(97, 123)))  # ASCII values for lowercase letters from 'a' (97) to 'z' (122)

# Combine all characters into a single password list
password = symbol + digit + upper + lower

# Shuffle the password list to randomize the order of characters
random.shuffle(password)

# Convert the list of characters into a string
password = ''.join(password)

# Print the generated password
print(password)

