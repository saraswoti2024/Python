#types of attribute and methods
#attribute- variable define -> instance

#instance-> always self parameter aune , 
#aautai class ko value multiple object banauda same hunxa twra object mai change garyam intialize gardem vanae teslai matrai use hunxa ani aaru object ko value class kai hunxa default

#default constructor
# class A:
#     def __init__(self):
#         self.name = "sara"
#         self.age = 20

#     def show(self):
#         print(self.name,self.age)

# a = A()
# a.name = "saraswoti"
# a.show()

# b = A()
# b.show()


# #multiple parameters, parameterized constructor
# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def show(self):
#         print(self.name,self.age)

# a = student("parbati",25) #passing value here
# a.show()
        

#class method-> cls, class name use garerw  nai call garinxa

# class class1:
#     school = "united"

#     # def __init__(self):
#     #     self.name = "saraswoti"
    
#     # def show(self):
#     #     print(self.name)
    
#     @classmethod
#     def display(cls,newname):
#         cls.school = newname
#         print(cls.school)

# a = class1()
# a.display("newsumit")
# # print(class1.school)

# b = class1()
# b.display("ambition")
# # print(b.school)

# c = class1()
# print(c.school)


#static method-> aauta default paramerter hunai parxa class vitrw ko value call garna so staticmethod use garyo vanae chahi parena works as both cls,self default
class A:
    @staticmethod
    def show(a,b):
        print(a+b)

a = A()
a.show(2,3)