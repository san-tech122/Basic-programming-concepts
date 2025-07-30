# conditions.py
"""
Author: Sanjay (san-tech122)
Description:
  This file covers conditional statements in Python:
  - if
  - if-else
  - if-elif-else
  - Nested if statements
  These allow programs to make decisions based on different conditions.
"""

# ========================
# ✅ 1. BASIC IF STATEMENT
# ========================
# Executes the code block if the condition is True

age = 20

if age >= 18:
    print("You are eligible to vote.")  # Output will show this because age is 20

# =============================
# 🔁 2. IF-ELSE STATEMENT
# =============================
# Runs one block if condition is True, another block if it's False

marks = 45

if marks >= 50:
    print("You passed the exam.")
else:
    print("You failed the exam.")  # Output will show this because 45 < 50

# ================================
# 🔄 3. IF-ELIF-ELSE STATEMENT
# ================================
# Checks multiple conditions in sequence

temperature = 30

if temperature > 35:
    print("It's too hot!")
elif temperature >= 25:
    print("The weather is pleasant.")  # This will be printed
elif temperature >= 15:
    print("It’s a bit cold.")
else:
    print("It’s freezing!")

# ========================
# 🔂 4. NESTED IF STATEMENT
# ========================
# An if statement inside another if

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful!")  # Both conditions are true
    else:
        print("Incorrect password.")
else:
    print("Invalid username.")

# ========================
# 🧠 5. USE WITH BOOLEAN
# ========================

is_student = True
has_id = False

if is_student and has_id:
    print("You can enter the library.")
else:
    print("Access denied.")  # One condition is False, so access denied

# ========================
# 🔍 6. COMPARISON INSIDE IF
# ========================

x = 10
y = 20

if x < y:
    print("x is less than y")  # True
if x != y:
    print("x is not equal to y")  # True