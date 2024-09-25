import random
import string

# def generate_pswd():
#     up_letters = random.choices(string.ascii_uppercase,k=2)
#     digit = random.choices(string.digits,k=1)
#     spsym = random.choices(string.punctuation,k=1)
#     others = random.choices(string.ascii_letters + string.digits + string.punctuation,k=6)
#     password_list = up_letters + digit + spsym+ others
#     # random.shuffle(password_list)
    
#     # return ''.join(password_list)
#     print(password_list)
    
# print("Password:", generate_pswd())

'''
string.ascii_lowercase: (‘a’ to ‘z’)
string.ascii_letters: (string.ascii_lowercase + string.ascii_uppercase)
string.digits: (string ‘0123456789’)
string.punctuation: (string of ASCII characters that are considered punctuation characters)
string.whitespace: (includes characters like space, tab, linefeed, return, formfeed, and vertical tab)
string.printable: (digits, letters (both uppercase and lowercase), punctuation, and whitespace characters)
'''