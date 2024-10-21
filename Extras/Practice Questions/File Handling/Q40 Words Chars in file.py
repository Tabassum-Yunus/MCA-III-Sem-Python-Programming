'''     Write a python program to count number of lines, words, characters, alphabets and digits in file.   '''

f = open('MyFile.txt', 'w+')
f.write('This is my first file\n')
f.write('This is second line\n')
f.write('\n')
f.write('Last line')
f.close()



f = open('D:\MyVScodeProgs\Programs\Python\Extras\Practice Questions\MyFile.txt', 'r+')
sen = f.readlines()
print(sen)
print('Number of lines: ', len(sen))
words = []
chars = 0
digits = alpha = 0
for i in sen:
    line = i.split() 
    for j in line:
        words.append(j)
        chars += len(j)
        j = j.lower()
        for k in j:
            if(ord(k) >= 97 and ord(k) <= 122):
                alpha += 1
            elif(ord(k) >= 48 and ord(k) <= 56):
                digits += 1
        
print(words)
print('Number of words: ', len(words))
print('Number of chars: ', chars)
print('Number of alpha: ', alpha)
print('Number of digits: ', digits)
f.close()

