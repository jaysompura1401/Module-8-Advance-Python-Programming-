# Q3. Write a Python program to open a file in write mode, write some text, and then close it.

# Program to open a file in write mode, write text, and close it

# Open the file in write mode ("w")
file = open("myfile.txt", "w")

# Write some text into the file
file.write("Hello, this is my first file handling program in Python.\n")
file.write("I am learning how to open, write, and close a file.\n")

# Close the file
file.close()

print("File written and closed successfully!")
