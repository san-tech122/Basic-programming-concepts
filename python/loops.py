# loops.py
"""
Author: Sanjay (san-tech122)
Description:
  This file explains Python loops in a beginner-friendly way:
  - for loops
  - while loops
  - range() function
  - break, continue, pass
  - nested loops
Loops are used to execute a block of code repeatedly.
"""

# ====================
# 🔁 1. FOR LOOP
# ====================
# Iterates over a sequence (like list, string, or range)

print("For Loop - Counting 1 to 5:")
for i in range(1, 6):
    print(i)

# Looping through a list
fruits = ["apple", "banana", "mango"]

print("\nFor Loop - Printing fruits:")
for fruit in fruits:
    print(fruit)

# Loop through string characters
name = "Sanjay"
print("\nFor Loop - Letters in name:")
for char in name:
    print(char)

# ====================
# 🔄 2. WHILE LOOP
# ====================
# Repeats as long as a condition is True

count = 1
print("\nWhile Loop - Counting till 5:")
while count <= 5:
    print(count)
    count += 1

# ================================
# 🔢 3. RANGE FUNCTION WITH FOR
# ================================
print("\nRange with for loop - Even numbers from 2 to 10:")
for i in range(2, 11, 2):
    print(i)  # prints 2, 4, 6, 8, 10

# ========================
# 🚪 4. BREAK STATEMENT
# ========================
print("\nBreak - Stop loop when fruit is banana:")
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)

# ============================
# 🔃 5. CONTINUE STATEMENT
# ============================
print("\nContinue - Skip banana:")
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# ============================
# 🧍 6. PASS STATEMENT
# ============================
# Does nothing, used as placeholder

for i in range(3):
    pass  # Reserved for future logic

# ============================
# 🔁 7. NESTED LOOPS
# ============================
print("\nNested Loop - Multiplication Table (1 to 3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("----------")

# =============================
# 📌 BONUS: LOOPING WITH ENUMERATE
# =============================
print("\nEnumerate - Get index while looping through fruits:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")