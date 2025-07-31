"""
sets.py
-------
This file explains the concept of **sets** in Python.

A **set** is an unordered collection of unique elements.
Sets are useful when you want to store items without duplicates and perform mathematical set operations like union, intersection, etc.

Syntax:
    my_set = {item1, item2, item3, ...}
"""

# 🔹 1. Creating a Set
fruits = {"apple", "banana", "cherry", "apple"}  # 'apple' will appear only once
print("Fruits set:", fruits)  # Output: Unordered, no duplicates

# 🔹 2. Creating an Empty Set
empty_set = set()
print("Empty set:", empty_set)

# Note: {} creates an empty dictionary, not a set.

# 🔹 3. Adding Elements
fruits.add("mango")
print("After adding mango:", fruits)

# 🔹 4. Updating Set With Multiple Items
fruits.update(["orange", "grape"])
print("After update:", fruits)

# 🔹 5. Removing Elements
fruits.remove("banana")  # Raises error if not found
print("After removing banana:", fruits)

fruits.discard("kiwi")  # No error even if 'kiwi' not found
print("After discarding kiwi (not in set):", fruits)

# 🔹 6. Popping an Element (removes random item)
removed_item = fruits.pop()
print("Popped item:", removed_item)

# 🔹 7. Clearing the Set
# fruits.clear()
# print("After clear:", fruits)  # Empty set

# 🔹 8. Looping Through a Set
colors = {"red", "green", "blue"}
for color in colors:
    print("Color:", color)

# 🔹 9. Set Length
print("Number of colors:", len(colors))

# 🔹 10. Set Operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("A union B:", A.union(B))           # {1, 2, 3, 4, 5, 6}
print("A intersection B:", A.intersection(B))  # {3, 4}
print("A difference B:", A.difference(B))      # {1, 2}
print("A symmetric difference B:", A.symmetric_difference(B))  # {1, 2, 5, 6}

# 🔹 11. Checking Membership
print("Is 3 in A?", 3 in A)

# 🔹 12. Set Comparisons
X = {1, 2}
Y = {1, 2, 3}

print("X is subset of Y:", X.issubset(Y))       # True
print("Y is superset of X:", Y.issuperset(X))   # True
print("X and Y are disjoint:", X.isdisjoint({4, 5}))  # True

# ✅ Summary:
# - Sets do NOT allow duplicates.
# - Sets are unordered and unindexed.
# - Great for filtering unique items and doing set math operations.
# - Faster than lists for membership tests.