# variables.py
# ---------------------------------------------
# Introduction to Python Variables
# This script covers how to declare, assign, and use variables in Python.
# Each section is commented for clarity.
# ---------------------------------------------

# 🔹 1. Variable Declaration and Assignment
name = "Sanjay"  # String variable (text)
age = 19         # Integer variable (whole number)
height = 5.9     # Float variable (decimal number)
is_student = True  # Boolean variable (True or False)

# 🔹 2. Print Variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is a student:", is_student)

# 🔹 3. Variable Naming Rules
# - Must start with a letter or underscore
# - Cannot start with a number
# - Can contain letters, numbers, and underscores
# - Are case-sensitive (age ≠ Age)

# Valid variable names
user_name = "santech"
_userAge = 20
user2 = "test"

# Invalid variable names (uncomment to test the error)
# 2user = "Invalid"   ❌ starts with number
# user-name = "Invalid" ❌ contains hyphen

# 🔹 4. Updating Variables
age = age + 1  # Now age is 20
print("Updated Age:", age)

# 🔹 5. Multiple Assignment
a, b, c = 10, 20, 30
print("a:", a, "| b:", b, "| c:", c)

# 🔹 6. Dynamic Typing
# Python allows reassigning variable with different type
x = 10         # int
print("x =", x, "→ type:", type(x))
x = "Ten"      # now str
print("x =", x, "→ type:", type(x))

# 🔹 7. Constants (by convention)
PI = 3.14159  # constant value (not enforced, but should not be changed)
print("Constant PI:", PI)

# ---------------------------------------------
# End of variables.py
# ---------------------------------------------