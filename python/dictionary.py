"""
dictionary.py
-------------
This file explains **dictionaries** in Python.

A **dictionary** is an unordered collection of key-value pairs.
Each key must be unique, and keys are used to access values quickly.

Syntax:
    my_dict = {
        "key1": value1,
        "key2": value2,
        ...
    }
"""

# 🔹 1. Creating a Dictionary
student = {
    "name": "Sanjay",
    "age": 18,
    "course": "B.Sc Computer Science",
    "is_active": True
}

print("Student Info:", student)

# 🔹 2. Accessing Values
print("Name:", student["name"])
print("Course:", student.get("course"))  # get() avoids error if key doesn't exist

# 🔹 3. Adding New Key-Value Pairs
student["college"] = "Yuvakshetra Institute"
print("After adding college:", student)

# 🔹 4. Modifying Existing Values
student["age"] = 19
print("Updated age:", student)

# 🔹 5. Removing Elements
student.pop("is_active")         # Removes specific key
print("After pop:", student)

del student["course"]            # Another way to remove
print("After del:", student)

# 🔹 6. Looping Through Dictionary
print("\nKeys and Values:")
for key, value in student.items():
    print(f"{key}: {value}")

print("\nKeys only:")
for key in student.keys():
    print(key)

print("\nValues only:")
for value in student.values():
    print(value)

# 🔹 7. Dictionary Length
print("Number of fields:", len(student))

# 🔹 8. Nested Dictionaries
users = {
    "user1": {"name": "Alice", "email": "alice@example.com"},
    "user2": {"name": "Bob", "email": "bob@example.com"},
}

print("Nested user2 name:", users["user2"]["name"])

# 🔹 9. Dictionary Methods
student.clear()         # Removes all items
print("Cleared student dict:", student)

# 🔹 10. Creating Dictionary from List of Tuples
pair_list = [("brand", "BMW"), ("model", "X5")]
car = dict(pair_list)
print("Car dictionary:", car)

# ✅ Summary:
# - Dictionaries store data as key-value pairs.
# - Keys must be unique and immutable (strings, numbers, tuples).
# - Great for fast lookups, organizing structured data, and nesting data.
# - Very useful in real-world applications like JSON APIs, databases, etc.