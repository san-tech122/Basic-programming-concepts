# operators.py
"""
Author: Sanjay (san-tech122)
Description:
  This file explains all the major types of operators in Python with examples.
  Operators are symbols used to perform operations on variables and values.
"""

# ==========================
# ➕ 1. ARITHMETIC OPERATORS
# ==========================
# Used to perform mathematical operations.

a = 10
b = 3

print("Addition (a + b):", a + b)
print("Subtraction (a - b):", a - b)
print("Multiplication (a * b):", a * b)
print("Division (a / b):", a / b)
print("Floor Division (a // b):", a // b)  # Removes decimal
print("Modulus (a % b):", a % b)           # Remainder
print("Exponentiation (a ** b):", a ** b)  # Power (10^3)

# ==========================
# 🟰 2. ASSIGNMENT OPERATORS
# ==========================
# Used to assign values to variables.

x = 5
x += 3  # Same as x = x + 3
print("After += 3, x =", x)

x -= 2  # x = x - 2
print("After -= 2, x =", x)

x *= 4  # x = x * 4
print("After *= 4, x =", x)

x /= 3  # x = x / 3
print("After /= 3, x =", x)

# ================================
# 🤔 3. COMPARISON OPERATORS
# ================================
# Used to compare values and return a Boolean (True or False).

p = 10
q = 20

print("Is p equal to q? (p == q):", p == q)
print("Is p not equal to q? (p != q):", p != q)
print("Is p greater than q? (p > q):", p > q)
print("Is p less than or equal to q? (p <= q):", p <= q)

# ===========================
# 🔗 4. LOGICAL OPERATORS
# ===========================
# Used to combine conditional statements.

is_coding = True
is_sleepy = False

print("AND (is_coding and is_sleepy):", is_coding and is_sleepy)
print("OR (is_coding or is_sleepy):", is_coding or is_sleepy)
print("NOT (not is_coding):", not is_coding)

# ================================
# 👀 5. IDENTITY OPERATORS
# ================================
# Compare memory locations, not just value.

a = [1, 2]
b = a
c = [1, 2]

print("a is b:", a is b)     # True (same memory)
print("a is c:", a is c)     # False (same value, different memory)
print("a is not c:", a is not c)

# ================================
# 📦 6. MEMBERSHIP OPERATORS
# ================================
# Test if a value is present in a sequence (like a list or string)

colors = ["red", "blue", "green"]
print("'red' in colors:", 'red' in colors)
print("'yellow' not in colors:", 'yellow' not in colors)