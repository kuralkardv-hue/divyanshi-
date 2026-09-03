# Program to perform various operations on Python Lists

# Creating a list
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# Append an element
numbers.append(60)
print("After append:", numbers)

# Insert an element
numbers.insert(2, 25)
print("After insert:", numbers)

# Remove an element
numbers.remove(40)
print("After remove:", numbers)

# Pop an element
numbers.pop()
print("After pop:", numbers)

# Extend the list
numbers.extend([70, 80])
print("After extend:", numbers)

# Sort the list
numbers.sort()
print("After sort:", numbers)

# Reverse the list
numbers.reverse()
print("After reverse:", numbers)

# Find length of list
print("Length of list:", len(numbers))

# Find maximum and minimum values
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))

# Count an element
print("Count of 20:", numbers.count(20))

# Find index of an element
print("Index of 30:", numbers.index(30))

# Clear the list
numbers.clear()
print("After clear:", numbers)