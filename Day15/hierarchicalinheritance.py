##one parent and multiple childs

class Human:
    def eat(self):
        print("i can eat")

class female(Human):
    def hello(self):
        print("hello i am female")

class male(Human):
    def hello1(self):
        print("hello i am male")

#derived 1
# female1 = female()
# female1.eat()
# female1.hello()

#derived 2
male1 = male()
male1.eat()
male1.hello1()
male1.hello()
