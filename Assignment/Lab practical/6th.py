#Q6. Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).
# Program: Simple Calculator with Exception Handling

try:
    # Taking inputs from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Taking operation input
    op = input("Enter operation (+, -, *, /): ")

    # Performing calculation
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2   # May raise ZeroDivisionError
    else:
        print("Invalid operation!")
        result = None

    # Print result if valid
    if result is not None:
        print(f"Result: {num1} {op} {num2} = {result}")

# Handling division by zero
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Handling invalid input (like entering text instead of number)
except ValueError:
    print("Error: Invalid input! Please enter numbers only.")

