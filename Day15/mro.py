# In Python, MRO determines the order in which methods are inherited and executed when a class has multiple parents. You can check MRO using:

class Teacher:
    def work(self):
        print("Teaching students and preparing lesson plans.")

class Researcher:
    def work(self):
        print("Conducting research and publishing papers.")

class Professor(Teacher, Researcher):  # Multiple Inheritance
    def work(self):
        print("Balancing teaching, research, and administrative duties.")

# Check MRO
print(Professor.mro())
#output:[<class '__main__.Professor'>, <class '__main__.Teacher'>, <class '__main__.Researcher'>, <class 'object'>]

#Implement a Parent1 and Parent2 class, both with an info() method. Derive a Child class and use super() to access both parent methods.
class Parent1:
    def info(self):
        print("This is Parent1's info method.")

class Parent2:
    def info(self):
        print("This is Parent2's info method.")

class Child(Parent1, Parent2):  # Multiple Inheritance
    def info(self):
        print("This is Child's info method.")
        super().info()  # Calls Parent1's info() due to MRO
        Parent2.info(self)  # Explicitly calling Parent2's info()

# Creating an object of Child
c = Child()

print("\nCalling Child's info():")
c.info()

#output
# Calling Child's info():
# This is Child's info method.
# This is Parent1's info method.
# This is Parent2's info method.
