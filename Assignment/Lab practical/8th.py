# Q8. Write a Python program to create a class and access its properties using an object.
# Program: Create a class and access its properties using an object

# Defining a class
class Student:
    # Class constructor
    def __init__(self, name, age, course):
        self.name = name      # property 1
        self.age = age        # property 2
        self.course = course  # property 3

# Creating an object of Student class
student1 = Student("Jay Sompura", 22, "Python Programming")

# Accessing properties using object
print("Student Name:", student1.name)
print("Student Age:", student1.age)
print("Enrolled Course:", student1.course)
