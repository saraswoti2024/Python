# Create a parent class Person with attributes name and age. Create a child class Student that inherits Person and adds an attribute grade. Display the details using a method.

# class Person:
#      def __init__(self,name,age):
#           self.name = name
#           self.age = age

# class Student(Person):
     
#      def __init__(self, name, age,grade):
#           super().__init__(name, age)
#           self.grade = grade

#      def display(self):
#           print(f"name = {self.name}, age = {self.age}, grade = {self.grade}")

# student1 = Student(name="saraswoti",grade=22,age=15)
# student1.display()

#singleinheritance
#Build a Employee class with attributes name and salary. Create a derived class Manager that adds department. Implement a method to calculate the bonus.               

# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary

#     def display(self):
#         print(f"name = {self.name},salary = {self.salary}")

# class Manager(Employee):

#     def __init__(self, name, salary,department):
#         super().__init__(name, salary)
#         self.department = department

#     def  bonuscalculation(self):
#         self.bonus = 0
#         if self.department=="development":
#             self.bonus = 15000
#             self.salary = self.salary + self.bonus
#         elif self.department=="buisness":
#             self.bonus = 10000
#             self.salary +=self.bonus
            
#         else:
#             self.bonus = 2000
#             self.salary += self.bonus

#     def display(self):
#         super().display()
#         print(f"bonus = {self.bonus}")

# #overidding vako show gareko
# emp1 = Employee(name="saraswoti",salary=50000)
# emp1.display()

# obj1 = Manager(name="saraswoti",salary=50000,department="cook")
# obj1.bonuscalculation()
# obj1.display()

##multiinheritance


# Design a SmartPhone class that inherits from both Camera and Phone. Implement methods like take_photo() and make_call().

# class Camera:
#     def take_photo(self):
#         print("i take picture")

# class Phone:
#     def make_call(self,number):
#         self.number = number
#         print(f"calling {number}")

# class SmartPhone(Camera,Phone):
#     def display(self):
#         print("i am AI assistant")
#         self.take_photo()
#         self.make_call(981123456)
        

# sm1 = SmartPhone()
# sm1.display()