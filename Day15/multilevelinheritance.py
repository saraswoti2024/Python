##multiple children and one parent, where derived children bata aaru children class haru banaunae
#parentclass-> class1, derivedclass(parentclassforclass3)->class2, derivedclassusingclass2->class3(class3 now can inherite properties of class1,class2) and so on


##mro-> son->mother(parent)->grandfather(aarko indirect parent)->so on
class Grandfather:

    def __init__(self,name):
        self.son = 2
        self.daughter = 3
        self.name = name

    def eat(self):
        print("i am grandfather")

    ##overriding
    def work(self):
        print("i can work grandfather")

class mother(Grandfather):

    def __init__(self, position):
        self.position = position

    def birth(self):
        print("i gave you birth, iam your mother")
    def work(self):
        print("i can work mother")
    

class son(mother):
    def __init__(self, position,name,talent):
        mother.__init__(self,position)
        Grandfather.__init__(self,name)
        self.talent = talent

    def display(self):
        print(f"son={self.talent}, mother = {self.position}, grandfather = {self.name}")

    def born(self):
        print("i am son")

    ##can call each overide method yesari
    def work(self):
        super().work()
        Grandfather.work(self)
        print("i can work son")

son1 = son(name="hari",position="2nddaughter",talent="football")
# son1.eat()
# son1.work()
son1.display()