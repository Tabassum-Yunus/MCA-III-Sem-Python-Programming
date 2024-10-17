'''     Write a program to read a string and find numbers of digits and alphabets.      '''

st = input('Enter a string: ')
st = st.lower()
digits = alpha = 0
for i in st:
    if(ord(i) >= 48 and ord(i) <= 56):
        digits += 1
    elif(ord(i) >= 97 and ord(i) <= 122):
        alpha += 1

print(st)
print('Digits: ', digits)
print('Alphabets: ', alpha)