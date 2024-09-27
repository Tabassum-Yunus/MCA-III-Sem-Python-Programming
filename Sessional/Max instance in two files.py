'''     Consider two text files with some content. Write a python program that finds the word in each file,
which is having maximum instances in another file. Suppose two existing files are file A and file B.
So you need to find a word from file A, which is having maximum instances in file B and in similar 
fashion, find a word from file B, which is having maximum instances in file a.'''


# Open the input files for reading
fh1 = open('D:\\MyVScodeProgs\\Programs\\Python\\Sessional\\FileA.txt', 'r') 
fh2 = open('D:\\MyVScodeProgs\\Programs\\Python\\Sessional\\FileB.txt', 'r')  

fileA_dict = dict()
fileB_dict = dict()

while(True):
    fileA_line = fh1.readline()  
    fileB_line = fh2.readline()  

    if(fileA_line != ''):
        list = fileA_line.split()
        for i in list:
            fileA_dict[i] = fileA_dict.get(i,0) + 1
    
    if(fileB_line != ''):
        list = fileB_line.split()
        for i in list:
            fileB_dict[i] = fileB_dict.get(i,0) + 1
    
    if fileA_line == '' and fileB_line == '':
        break  

print(fileA_dict)
print()
print(fileB_dict)
m = 0
for fileA_key,fileA_value in fileA_dict.items():
    for fileB_key,fileB_value in fileB_dict.items():
        if(fileA_key==fileB_key):
            if(fileB_value > m):
                m = fileB_value
                wordA = fileB_key

print('Word of File A having maximum frequency in File B: ',wordA)

m = 0
for fileB_key, fileB_value in fileB_dict.items():
    for fileA_key, fileA_value in fileA_dict.items():
        if(fileB_key==fileA_key):
            if(fileA_value > m):
                m = fileA_value
                wordB = fileA_key

print('Word of File B having maximum frequency in File A: ',wordB)