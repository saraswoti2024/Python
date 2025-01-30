# Create a parent class Person with attributes name and age. Create a child class Student that inherits Person and adds an attribute grade. Display the details using a method.

class Person:
     def __init__(self,name,age):
          self.name = name
          self.age = age

class Student(Person):
     
     def __init__(self, name, age,grade):
          super().__init__(name, age)
          self.grade = grade

     def display(self):
          print(f"name = {self.name}, age = {self.age}, grade = {self.grade}")

student1 = Student(name="saraswoti",grade=22,age=15)
student1.display()

               

     
