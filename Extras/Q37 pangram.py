'''     Write a program in python to check whether a sentence is pangram or not. 
  A pangram, or holo-alphabetic sentence, is a sentence that contains every letter of the alphabet at least once.    '''

st = input('Enter a string: ')
st = st.lower()
d = dict()

for i in st:
    if(ord(i) >= 97 and ord(i) <= 122):
        d[i] = d.get(i,0)+1
print(d)
if(len(d) == 26):
    print('Pangram')
else:
    print('Not')
