'''     Write a function to add arbitrary integers.     '''

def addition(*k):
    sum = 0
    for i in k:
        sum += i
    return sum

l = input('Numbers with space: ')
l1 = list(map(int, l.split()))

# unpacks the list and passes each element as an argument to the add_integers() function. 
# Without the *, it would pass the list as a single argument, which would result in an error.
result = addition(*l1)