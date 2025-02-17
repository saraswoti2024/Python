###in encapsulation we can use getter and setter method to access and modify private attributes and methods
##it is a good practice use getter and setter to modify or display private values instead of name mangling haru use this only this!!!!! 
##encapsulation implements abstraction, provides more security, readable code

class Student:
    def __init__(self,name,age,gender):
        self.name = name
        self.__age = age
        self._gender = gender
    
    #private method
    def __display(self):
        print(f"name is : {self.name} , age : {self.__age}, gender : {self._gender}")

    #getter-> display
    def get_value(self):
        # print(self.__age) #direct print garda ni hunxa
        return self.__display() ##method use private
        # return self.__age
            
    #setter-> modify,edit attributes
    def set_value(self,age):
        self.__age = age


S1 = Student("saraswoti",22,"F")
S1.get_value() #method
# print(S1.get_value()) ##attribute
S1.set_value(33) 
S1.get_value()  #method
# print(S1.get_value()) ##attribute