'''     Write a Python program that first accept a string and If the string length is less than 4, 
        return empty string. Then create a string made of the first 2 and the last 2 chars from 
        the accepted string.     '''

def concatChars(str):
    if(len(str) <= 4):
        return None
    return str[:2]+str[len(str)-2:]

st = input('Enter string: ')
result = concatChars(st)
print(result)