"""
lists.py
--------
This file covers the concept of **lists** in Python.
A list is an ordered, mutable collection of items. Lists are widely used in Python to store sequences of data.

Syntax:
    my_list = [item1, item2, item3, ...]
"""

# 🔹 1. Creating a List
fruits = ["apple", "banana", "cherry", "mango"]
print("Fruits:", fruits)

# 🔹 2. Accessing List Elements (Indexing)
print("First fruit:", fruits[0])       # apple
print("Last fruit:", fruits[-1])       # mango

# 🔹 3. Slicing a List
print("First 2 fruits:", fruits[:2])   # ['apple', 'banana']

# 🔹 4. Modifying List Items
fruits[1] = "blueberry"
print("Modified fruits:", fruits)

# 🔹 5. Adding Items
fruits.append("orange")                # Adds at the end
print("After append:", fruits)

fruits.insert(2, "grape")              # Inserts at index 2
print("After insert:", fruits)

# 🔹 6. Removing Items
fruits.remove("cherry")               # Removes 'cherry'
print("After remove:", fruits)

popped_fruit = fruits.pop()           # Removes last item
print("Popped fruit:", popped_fruit)

# 🔹 7. Length of List
print("Number of fruits:", len(fruits))

# 🔹 8. Looping Through a List
print("List of fruits:")
for fruit in fruits:
    print("-", fruit)

# 🔹 9. Checking If Item Exists
if "apple" in fruits:
    print("Apple is in the list.")

# 🔹 10. Sorting a List
numbers = [5, 2, 9, 1, 7]
numbers.sort()  # Ascending order
print("Sorted numbers:", numbers)

numbers.sort(reverse=True)  # Descending
print("Descending numbers:", numbers)

# 🔹 11. Copying a List
copy_list = fruits.copy()
print("Copied list:", copy_list)

# 🔹 12. List Comprehension (Shortcuts for loops)
squares = [x**2 for x in range(6)]
print("Squares using list comprehension:", squares)

# 🔹 13. Nested Lists (Lists inside a list)
matrix = [[1, 2], [3, 4], [5, 6]]
print("Matrix element [1][0]:", matrix[1][0])  # Output: 3

# ✅ Summary:
# - Lists are used to store multiple values in one variable.
# - They are ordered and changeable (mutable).
# - Python provides many built-in functions and methods for working with lists.