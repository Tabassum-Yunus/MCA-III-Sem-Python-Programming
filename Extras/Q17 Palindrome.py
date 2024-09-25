'''     Write Python Program to Check Whether a String is Palindrome or Not     '''

str = input('Enter string: ')
length = len(str)
for i in range(length//2):
    if(str[i] != str[length-i-1]):
        print(str, 'is not palindrome')
        break
else:
    print(str, 'is palindrome')