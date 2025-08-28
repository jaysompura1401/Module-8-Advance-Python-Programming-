#Q5. Write a Python program to write multiple strings into a file. 

# Program to write multiple strings into a file

# Open file in write mode
file = open("multilines.txt", "w")

# List of strings
lines = [
    "Python is a powerful programming language.\n",
    "It is widely used in web development, data science, and AI.\n",
    "File handling is an important part of Python programming.\n",
    "This is an example of writing multiple strings into a file.\n"
]

# Write all strings to file
file.writelines(lines)

# Close the file
file.close()

print("Multiple strings written to file successfully!")
