##one parent and multiple childs

class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def access(self):
        print(f"name: {self.name}, age = {self.age},address = {self.address}")
        
    def eat(self):
        print("i can eat")

class female(Human):
    def __init__(self, name, age,address):
        super().__init__(name, age)
        self.address = address

    def hello(self):
        print("hello i am female")

class male(Human):
    def __init__(self, name, age,address):
        super().__init__(name, age)
        self.address= address
    def hello1(self):
        print("hello i am male")


#male and female dont have any connection here so attribute ni female rw parent ko j xa tahi testai 
#derived 1
female1 = female("sara",20,"gothatar")
# female1.eat()
# female1.hello()
female1.access()

#derived 2
male1 = male("ram","20","shantinagar")
# # male1.eat()
# # male1.hello1()
# # male1.hello()
male1.access()
