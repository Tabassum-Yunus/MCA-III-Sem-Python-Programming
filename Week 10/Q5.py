'''     Write a program in python to find word/s having maximum number of instances in a given file and 
        replace all its occurrences with “Aligarh”.     '''

words = {}
max_occ_wors = []
file = open('D:\MyVScodeProgs\Programs\Python\Week 10\MyFile.txt', 'r')
for line in file:
    splitted_line = line.split()
    for word in splitted_line:
        words[word] = words.get(word, 0) + 1
print(words)
occ_set = set(words.values())
print(occ_set)
occ_list = sorted(list(occ_set))
print(occ_list)
max = occ_list[-1]
print(max)

for key, value in words.items():
    if(value == max):
        max_occ_wors.append(key)

file.seek(0,0)
content = file.readlines()
print('Content:', content)

for i in range(len(content)):
    splitted = content[i].split()
    line = ''
    for j in range(len(splitted)):
        if(splitted[j] in max_occ_wors):
            splitted[j] ='Aligarh'
        line += splitted[j] + ' '
    content[i] = line + '\n'
print(content)
file.close()




