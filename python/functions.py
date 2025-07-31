"""
functions.py
------------
This file explains the concept of **functions** in Python using clear examples.
Functions are reusable blocks of code designed to perform a specific task.
They help make your programs cleaner, shorter, and easier to understand.
"""

# 🧠 1. Basic Function Without Parameters
def greet():
    print("Hello, welcome to the world of Python functions!")

greet()  # Calling the function

# 🧠 2. Function With Parameters
def greet_user(name):
    print(f"Hello {name}, glad to have you here!")

greet_user("Sanjay")  # Output: Hello Sanjay, glad to have you here!

# 🧠 3. Function With Return Value
def add(a, b):
    return a + b

result = add(10, 5)
print("Sum is:", result)

# 🧠 4. Default Parameter Value
def power(base, exponent=2):
    return base ** exponent

print(power(3))       # Output: 9 (3^2)
print(power(2, 5))    # Output: 32 (2^5)

# 🧠 5. Keyword Arguments
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(pet_name="Bruno", animal_type="dog")

# 🧠 6. Variable Number of Arguments (*args)
def print_fruits(*fruits):
    print("Fruits I like:")
    for fruit in fruits:
        print(f"- {fruit}")

print_fruits("apple", "banana", "mango")

# 🧠 7. Variable Number of Keyword Arguments (**kwargs)
def print_profile(**info):
    print("Profile Info:")
    for key, value in info.items():
        print(f"{key}: {value}")

print_profile(name="Sanjay", age=18, country="India")

# 🧠 8. Nested Functions
def outer():
    def inner():
        print("This is the inner function.")
    print("This is the outer function.")
    inner()

outer()

# 🧠 9. Lambda Function (anonymous function)
square = lambda x: x * x
print("Square of 6 is:", square(6))

# 🧠 10. Function Documentation (docstring)
def multiply(x, y):
    """
    This function multiplies two numbers and returns the result.
    Parameters:
        x (int or float)
        y (int or float)
    Returns:
        int or float
    """
    return x * y

print(multiply(4, 3))  # Output: 12

# ✅ Conclusion:
# Functions make code reusable and organized.
# Always give meaningful names to functions.
# Use docstrings to explain what a function does, especially in larger projects.