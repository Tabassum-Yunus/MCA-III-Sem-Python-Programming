'''     Consider two files having some lines of statements. Write a Python program to swap content 
        present at middle line of first file with the content of last line of the second file. 
        (Note: First file contains odd numbers of lines of statement)     '''

fh1 = open('File1_W7Q6.txt', 'r+')
fh2 = open('File2_W7Q6.txt', 'r+')

f1_lines = fh1.readlines()
f2_lines = fh2.readlines()
print(f1_lines)
print(f2_lines)

fh1.close()
fh2.close()

fh1 = open('File1_W7Q6.txt', 'w')
fh2 = open('File2_W7Q6.txt', 'w')

mid_line_File1 = f1_lines[len(f1_lines)//2]
end_line_File2 = f2_lines[len(f2_lines)-1]
print(mid_line_File1)
print(end_line_File2)

mid_line_File1, end_line_File2 = end_line_File2, mid_line_File1
print(mid_line_File1)
print(end_line_File2)

print(f1_lines)
print(f2_lines)

fh1.writelines(f1_lines)
fh2.writelines(f2_lines)

fh1.close()
fh2.close()
