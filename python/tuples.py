"""
tuples.py
---------
This file introduces **tuples** in Python.

Tuples are used to store multiple items in a single variable, just like lists.
But unlike lists, **tuples are immutable**, meaning you can't change their values after creation.

Syntax:
    my_tuple = (item1, item2, item3, ...)
"""

# 🔹 1. Creating Tuples
fruits = ("apple", "banana", "cherry")
print("Fruits Tuple:", fruits)

# 🔹 2. Single Item Tuple (Must include a comma!)
single = ("apple",)
print("Single item tuple:", single)

# Without the comma, it's just a string:
not_a_tuple = ("apple")
print("Type of not_a_tuple:", type(not_a_tuple))  # str

# 🔹 3. Accessing Tuple Elements (Indexing)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 🔹 4. Slicing Tuples
print("First two fruits:", fruits[:2])

# 🔹 5. Looping Through Tuples
for fruit in fruits:
    print("Fruit:", fruit)

# 🔹 6. Checking if Item Exists
if "banana" in fruits:
    print("Banana is in the tuple.")

# 🔹 7. Tuple Length
print("Tuple length:", len(fruits))

# 🔹 8. Nested Tuples
nested = ("apple", ("banana", "cherry"), "mango")
print("Nested element:", nested[1][1])  # Output: cherry

# 🔹 9. Tuple Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
combined = tuple1 + tuple2
print("Combined tuple:", combined)

# 🔹 10. Tuple Repetition
repeat = ("Hi",) * 3
print("Repeated tuple:", repeat)

# 🔹 11. Tuple vs List
# Tuples are:
# - Immutable
# - Faster than lists
# - Useful for fixed collections (like coordinates, days of the week)

# 🔹 12. Converting Between Tuple and List
list_version = list(fruits)
list_version.append("orange")
print("List version:", list_version)

tuple_again = tuple(list_version)
print("Back to tuple:", tuple_again)

# ✅ Summary:
# - Use tuples when data shouldn’t change.
# - They use less memory than lists and protect data integrity.
# - Parentheses are used, but the **comma** defines a tuple.