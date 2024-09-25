'''     Write a program that inputs a main string and then creates an encrypted string
        by embedding a short symbol-based string after each character. The program
        should also be able to produce the decrypted string from encrypted string.      '''


# Accept the original string from the user
str = input('Enter a string: ')

# Accept the symbol(s) to embed between the characters
symbol = input('Enter symbol(s) to embed in the string: ')

# Get the length of the symbol(s) to use for proper slicing during decryption
len_symbol = len(symbol)

# Initialize the encrypted and decrypted strings
encrypted = ''
decrypted = ''

# Encrypt the string by appending each character followed by the symbol(s)
for i in str:
    encrypted += i + symbol

# Output the encrypted string
print('Encrypted string: ', encrypted)

# Decrypt the string by skipping over the symbols
for i in range(0, len(encrypted), len_symbol + 1):
    decrypted += encrypted[i]

# Output the decrypted string, which should match the original string
print('Decrypted string: ', decrypted)
