#oop types
#1.Abstraction -> hiding the implementation details of a class and only showing the essential features to the user.
#2.Encapsulation-> wrapping data and functions into a single unit(object).
#3.Inheritance
#4.Polymorphism

#3.inheritance-> inheriting property from exisiting classes
#adv-> reusing of code instead of writing again and again
#existing main class -> base/parent/superclass
#made from exisiting class-> derived/child/sub

##syntax:
##class DerivedclassName(BaseClassName):
                ##classdefination/statements

#################################methods#################################
# class Human:
#     def eat(self):
#         print("i can eat")
#     def work(self):
#         print("i can work")

# class Male(Human):
#     def flirt(self):
#         print("i can flirt")
    
#     #we can modify yesari,it is overriding concept ani yahi call hunxa aaba 
#     def work(self):
#         super().work() #this prints baseclass ma vako method work pani ##super().methodname()
#         print("i can code")

# male1 = Male()
# male1.eat() #baseclass methods can be accessed now
# male1.flirt() #derivedclass
# male1.work()


######################attribute###################

class Human:
    def __init__(self,ears): #with parameters write in derived class as well
        self.eyes = 2
        self.nose = 2
        self.ears = ears

class Male(Human):
    
    def __init__(self,age,ear): #ear is parameter in order to access we need to write
        super().__init__(ear) #using baseclass attributes #need to write here as well
        
        self.name = "saraswoti"
        self.age = age

    def display(self):
        print(f"hi i am {self.name}, i have {self.ears} ears")

male1 = Male(22,2)
print(male1.nose)
print(male1.name)
print(male1.ears)
male1.display()