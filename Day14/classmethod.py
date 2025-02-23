
#####adding method to class##################
# class College:
#     total_student  = 100 #class object variable (global) #for every object the value of total_Student will be 100

#     def __init__(self,name,faculty):
#         self.name = name
#         self.faculty = faculty
    
#     #method in class (normal function banako)
#     #self keyword is necessary parameter inside class 
#     def display(self):
#         print(f"name is : {self.name}, faculty is {self.faculty},total_Student is {self.total_student}")

#     #returning value to object so that it can print there
#     def display2(self):
#         # print("hi")
#         return "hi"


# #object1
# College1 = College("Saraswoti", "Computer Science")
# print(College1.total_student)
# College1.display()
# # College1.display2()
# print(College1.display2())
# print()

# #object2
# College2 = College("parbati","BBA")
# College2.total_student = 20 #yesari manually change garyo vanae chahi yesko object ma change hunxa
# print(College2.total_student)
# print()

# #object3
# College3 = College("Saraswoti", "Computer Science")
# print(College3.total_student)
# # College1.display()

#################class method cls#########################
##normally self means we are passing object, here we pass class itself using cls
##cls vako thau ma class lai point garxa same as self vako thau ma object lai point gareko jastai

class student2:
    counter = 0

    def __init__(self,name):
        self.name = name
        student2.counter = student2.counter+1
    
    def msg(self):
        print(self.name,student2.counter)
    
    @classmethod
    def object_count(cls):
        return cls.counter

s1 = student2("saraswoti")
s2 = student2("parbati")
s3 = student2("laxman")
s1.msg()
print(student2.object_count())