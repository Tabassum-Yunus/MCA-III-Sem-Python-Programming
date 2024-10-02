'''     Consider two files having some lines of statements. Write a Python program to swap content 
        present at middle line of first file with the content of last line of the second file. 
        (Note: First file contains odd numbers of lines of statement)     '''

fh1 = open('D:\MyVScodeProgs\Programs\Python\Week 7\File1_W7Q6.txt', 'r+')
fh2 = open('D:\MyVScodeProgs\Programs\Python\Week 7\File2_W7Q6.txt', 'r+')

f1_lines = fh1.readlines()
f2_lines = fh2.readlines()
print('BEFORE SWAPPIPNG')
print('Content of file 1: ',f1_lines)
print('Content of file 2: ',f2_lines)

fh1.close()
fh2.close()

fh1 = open('File1_W7Q6.txt', 'w')
fh2 = open('File2_W7Q6.txt', 'w')

f1_lines[len(f1_lines)//2], f2_lines[len(f2_lines)-1] = f2_lines[len(f2_lines)-1], f1_lines[len(f1_lines)//2]

print('AFTER SWAPPIPNG')
print('Content of file 1: ',f1_lines)
print('Content of file 2: ',f2_lines)

fh1.writelines(f1_lines)
fh2.writelines(f2_lines)

fh1.close()
fh2.close()
