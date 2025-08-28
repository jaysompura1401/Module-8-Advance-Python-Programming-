# Q7. Write a Python program to demonstrate handling multiple exceptions.

# Program: Handling Multiple Exceptions

try:
    # Taking inputs
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Division operation (may raise ZeroDivisionError)
    result = num1 / num2

    # Accessing a list element (may raise IndexError)
    numbers = [10, 20, 30]
    index = int(input("Enter index (0-2) to access from the list: "))
    print("Value at index:", numbers[index])

    # Printing the division result
    print("Division Result:", result)

# Handling division by zero
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Handling invalid input
except ValueError:
    print("Error: Invalid input! Please enter numbers only.")

# Handling invalid list index
except IndexError:
    print("Error: Index out of range. Please enter a valid index (0-2).")

# Handling any other unexpected errors
except Exception as e:
    print("An unexpected error occurred:", e)
