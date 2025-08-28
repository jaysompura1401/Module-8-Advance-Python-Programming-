# Q2. Write a Python program to read a name and age from the user and print a formatted output.

# Taking input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Using format() method
print("Hello {}, you are {} years old.".format(name, age))

# Using f-string (recommended)
print(f"Hello {name}, you are {age} years old.")
