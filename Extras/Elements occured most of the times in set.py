# Define the three sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = {4, 5, 6, 7}

# Find elements that occur in at least two of the three sets
most_frequent_elements = ((a.intersection(b)).union(b.intersection(c))).union(a.intersection(c))
# (set1 & set2) | (set2 & set3) | (set1 & set3)

# Print the result
print("Elements that occur in most sets:", most_frequent_elements)