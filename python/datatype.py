# datatype.py
"""
Author: Sanjay (san-tech122)
Description:
  This file explains the fundamental data types in Python with examples.
  Understanding data types is crucial for mastering Python and writing clean, bug-free code.
"""

# =======================
# 📘 1. STRING
# =======================
# A sequence of characters enclosed in single or double quotes.
name = "Sanjay"
greeting = 'Hello, world!'
print("String Example:", name)
print("Greeting:", greeting)

# =======================
# 🔢 2. INTEGER (int)
# =======================
# Whole numbers without decimals.
age = 20
year = 2025
print("Integer Example - Age:", age)
print("Integer Example - Year:", year)

# =======================
# 🔣 3. FLOAT (float)
# =======================
# Numbers with decimal points.
price = 49.99
pi = 3.14159
print("Float Example - Price:", price)
print("Float Example - Pi:", pi)

# =======================
# ✅ 4. BOOLEAN (bool)
# =======================
# Only two possible values: True or False.
is_student = True
has_passport = False
print("Boolean Example - Is Student:", is_student)
print("Boolean Example - Has Passport:", has_passport)

# =======================
# 📋 5. LIST
# =======================
# An ordered, changeable collection. Duplicates allowed.
fruits = ["apple", "banana", "cherry"]
print("List Example:", fruits)
print("First Fruit:", fruits[0])  # Access by index

# =======================
# 📦 6. TUPLE
# =======================
# Ordered but unchangeable. Use when data shouldn't be modified.
coordinates = (10.5, 20.3)
print("Tuple Example:", coordinates)

# =======================
# 🔀 7. SET
# =======================
# Unordered collection with no duplicates.
unique_numbers = {1, 2, 3, 3, 4}
print("Set Example (no duplicates):", unique_numbers)

# =======================
# 🔑 8. DICTIONARY (dict)
# =======================
# Key-value pairs. Great for structured data.
student = {
    "name": "Sanjay",
    "age": 20,
    "course": "BSc CS"
}
print("Dictionary Example:", student)
print("Student Name:", student["name"])