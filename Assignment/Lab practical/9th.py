# Q9. Write Python programs to demonstrate different types of inheritance (single, multiple,multilevel, etc.).  
# Program to demonstrate different types of Inheritance in Python

# 1. Single Inheritance
class Parent:
    def display_parent(self):
        print("Single Inheritance → Parent class")

class Child(Parent):
    def display_child(self):
        print("Single Inheritance → Child class")


# 2. Multiple Inheritance
class Father:
    def skill_father(self):
        print("Multiple Inheritance → Father's Skill: Driving")

class Mother:
    def skill_mother(self):
        print("Multiple Inheritance → Mother's Skill: Cooking")

class Son(Father, Mother):
    def skill_son(self):
        print("Multiple Inheritance → Child's Skill: Dancing")


# 3. Multilevel Inheritance
class GrandParent:
    def show_grandparent(self):
        print("Multilevel Inheritance → Grandparent class")

class ParentLevel(GrandParent):
    def show_parent(self):
        print("Multilevel Inheritance → Parent class")

class ChildLevel(ParentLevel):
    def show_child(self):
        print("Multilevel Inheritance → Child class")


# 4. Hierarchical Inheritance
class CommonParent:
    def common_method(self):
        print("Hierarchical Inheritance → Common Parent class")

class ChildA(CommonParent):
    def show_childA(self):
        print("Hierarchical Inheritance → ChildA class")

class ChildB(CommonParent):
    def show_childB(self):
        print("Hierarchical Inheritance → ChildB class")


# 5. Hybrid Inheritance
class GP:
    def show_GP(self):
        print("Hybrid Inheritance → GrandParent class")

class P1(GP):
    def show_P1(self):
        print("Hybrid Inheritance → Parent1 class")

class P2(GP):
    def show_P2(self):
        print("Hybrid Inheritance → Parent2 class")

class HybridChild(P1, P2):   # Hybrid = Multiple + Multilevel
    def show_child(self):
        print("Hybrid Inheritance → Child class")


# ------------------------
# MAIN PROGRAM EXECUTION
# ------------------------

print("\n--- 1. Single Inheritance ---")
c = Child()
c.display_parent()
c.display_child()

print("\n--- 2. Multiple Inheritance ---")
s = Son()
s.skill_father()
s.skill_mother()
s.skill_son()

print("\n--- 3. Multilevel Inheritance ---")
cl = ChildLevel()
cl.show_grandparent()
cl.show_parent()
cl.show_child()

print("\n--- 4. Hierarchical Inheritance ---")
a = ChildA()
a.common_method()
a.show_childA()

b = ChildB()
b.common_method()
b.show_childB()

print("\n--- 5. Hybrid Inheritance ---")
hc = HybridChild()
hc.show_GP()
hc.show_P1()
hc.show_P2()
hc.show_child()
