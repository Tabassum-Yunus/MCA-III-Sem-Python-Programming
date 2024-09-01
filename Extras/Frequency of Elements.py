'''     Find the frequency of each element entered in list      '''



# Prompt the user to enter a list of integers separated by spaces.
user_input2 = input("Enter list of integers separated by space: ")

# Split the user input into a list of strings, then map each string to an integer to create a list of integers.
list1 = list(map(int, user_input2.split()))

# Convert the list of integers to a set to remove duplicates, then convert it back to a list to preserve the order.
mySet = set(list1)
unique = list(mySet)

# Initialize a list 'count' with None values to keep track of the count of each unique element.
count = [None] * len(unique)

# Set the initial count of each unique element to 0.
for i in range(len(unique)):
    count[i] = 0

# Iterate through the unique elements and the original list to count occurrences of each unique element.
for i in range(len(unique)):
    for j in range(len(list1)):

        # Compare each unique element with each element in the original list.
        if unique[i] == list1[j]:  

            # Increment the count if a match is found.
            count[i] += 1          

print('Number --> Frequency')
for i,j in zip(unique, count):
    print('\t',i,'\t\t',j)
