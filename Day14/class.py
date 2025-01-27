##we say #varibales->attribute, function-> methods coz it is associated with class and attached to objects ,it is not free floating like without class we did before,sabai class vitrw xa

## object another name instance

#class classname
# class CarDesign:
#     pass #statements

# # #object-> object_name = classname()
# obj1=CarDesign()
# obj2=CarDesign()
# print(type(obj1))
# print(type(obj2))

#adding attribute using __init__(self)-> works like constructor ,
# basically a constructor->#automatically object banaunae bitikai call hunxa , always take an parameter called self(builtin keyword) 

##self -> #object banauda self lai point garxa ani automatically call hunxa
##self parameter is a regerence to the current object(instance) of the class and is used to access variables that belongs to the class

# class Instructor:
#     def __init__(self): 
#        print(self)
        
# Instructor1 = Instructor() #yo banda self ma yo point hunxa ani object address same hunxa
# print(Instructor1)
# print()
# Instructor2 = Instructor()  #yo banda self ma yo point hunxa ani object address same hunxa
# print(Instructor2)


##without passing parameters(default constructor)

# class Instructor:
#     def __init__(self): 
#         print("without passing parameters")
#         self.followers = 0

# Instructor1 = Instructor()
# # Instructor1.followers=2
# print(Instructor1.followers) #0


##with passing parameters(parameterized constructor)

# class Instructor:
#     def __init__(self,name,address):
#         self.name1 = name #self.variable_name(any) = assigngareko_parameter ma vako
#         self.address1 = address
#         print("without passing parameters")
#         self.followers = 20 #yesari default value ni pass garna milxa without passing parameter

# Instructor1 = Instructor("saraswoti","shantinagar") 
# print(Instructor1.name1)
# print(Instructor1.address1)
# print(Instructor1.followers) 
# print()
# Instructor2 = Instructor("parbati","Gothatar")
# # Instructor2.name1 = "bimala" #change hunxa value, bimala aauxa
# print(Instructor2.name1)
# print(Instructor1.address1)
# print(Instructor1.followers)

