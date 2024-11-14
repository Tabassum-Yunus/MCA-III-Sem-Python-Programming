'''     Write a Python program to delete ‘e’ from the end of a given string (length should be at least 3)
        and add ‘en' at the end. If the string length of the given string is less than 3, leave it unchanged.     '''

def replace(s):
    length = len(s)
    if(length<3 or str[-1] != 'e'):
        return s

    return s[:length-1]+'en'

str = input('Enter string: ')
print(replace(str))