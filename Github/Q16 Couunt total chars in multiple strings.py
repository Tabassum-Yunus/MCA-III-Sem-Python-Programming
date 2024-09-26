'''     Write a function to receive multiple strings and count total characters.    '''

def count_total_characters(*args):
    chars = 0
    for i in args:
        chars += len(i)
    return chars

str = input('Enter multiple strings: ')
list1 = str.split()
total_characters = count_total_characters(*list1)
print(total_characters)