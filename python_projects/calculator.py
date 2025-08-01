# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

print("Welcome to Sanjay's Python Calculator 🔢")
print("Choose an operation: +, -, *, / or 'exit' to quit")

while True:
    op = input("\nEnter operation (+ - * /): ")
    
    if op.lower() == 'exit':
        print("Thanks for using the calculator. Goodbye!")
        break

    if op not in ['+', '-', '*', '/']:
        print("Invalid operation. Try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if op == '+':
        result = add(num1, num2)
    elif op == '-':
        result = subtract(num1, num2)
    elif op == '*':
        result = multiply(num1, num2)
    elif op == '/':
        result = divide(num1, num2)

    print("Result:", result)