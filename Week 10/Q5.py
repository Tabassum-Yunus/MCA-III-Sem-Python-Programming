'''     Write a program in python to find word/s having maximum number of instances in a given file and 
        replace all its occurrences with “Aligarh”.     '''

words_count = {}
max_occ_words = []
file = open('D:\MyVScodeProgs\Programs\Python\Week 10\MyFile.txt', 'r')
for line in file:
    words = line.split()
    for word in words:
        words_count[word] = words_count.get(word, 0) + 1
# print(words_count)
# print(words, '\n')
occ_set = set(words_count.values())
# print(occ_set)
occ_list = sorted(list(occ_set))
# print(occ_list)
max = occ_list[-1]
# print(max)

for key, value in words_count.items():
    if(value == max):
        max_occ_words.append(key)

print('Maximum occured word(s):',max_occ_words,'with the frequency of',max, '\n')
file.seek(0,0)

content = file.readlines()
# print('Content:', content, '\n')

for i in range(len(content)):
    splitted = content[i].split()
    line = ''
    for j in range(len(splitted)):
        if(splitted[j] in max_occ_words):
            splitted[j] ='Aligarh'
        line += splitted[j] + ' '
    content[i] = line + '\n'
# print(content)




file.close()



file = open('D:\MyVScodeProgs\Programs\Python\Week 10\MyFile.txt', 'w')

for i in content:
    file.write(str(i))

file.close()




