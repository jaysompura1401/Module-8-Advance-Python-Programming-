#Q10. Write Python programs to demonstrate method overloading and method overriding. 

# Program to demonstrate Method Overloading (using default arguments)

class Calculator:
    # Method with default arguments
    def add(self, a=0, b=0, c=0):
        return a + b + c

# Create object
calc = Calculator()

# Different ways of calling the same method
print("Addition of 2 numbers:", calc.add(10, 20))       # 2 arguments
print("Addition of 3 numbers:", calc.add(10, 20, 30))  # 3 arguments
print("Addition with 1 number:", calc.add(5))          # 1 argument


# Program to demonstrate Method Overriding

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    # Overriding parent method
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    # Overriding parent method
    def sound(self):
        print("Cat meows")

# Create objects
a = Animal()
d = Dog()
c = Cat()

a.sound()  # Parent class method
d.sound()  # Overridden method in Dog
c.sound()  # Overridden method in Cat
