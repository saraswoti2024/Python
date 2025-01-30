##inheritancing from two or more classses
##two or more parent class with single child class

class Human:
    def __init__(self,flesh):
        self.eyes = 2
        self.flesh = flesh

    def eat(self):
        print("i can eat")
    
    def work(self):
        print("i can work human")

class Female:
    def __init__(self,name):
        self.eyes = 5
        self.name = name

    def dance(self):
        print("i can dance")
    
    def work(self):
        print("i can work female")

class Girl(Human,Female):

    # def __init__(self,name,flesh):
    #     super().__init__(name)
    #     self.ears = 5

    def work(self):
        print("i can work derived")

    def display(self):
        print(self.eyes,self.ears)

Girl1 = Girl(name="sara",flesh="fresh")

##MRO method use 
#same method xa rey sabai class ma ani derived bata object banayerw call garyam vane derived class mai vako call hunxa, if derived ma xaina vane jun chahi aagadi class lekhyaxam derived ma tesko dekhauxa

Girl1.work()
Female.work(Girl1) #yesari we can access female class ko same method as aaru classes sanga ko match
Human.work(Girl1) #yesari we can acess human class ko same method as arru classes sanga ko match

Girl1.dance()
Girl1.eat()
Girl1.display()

##attributes
print(Girl1.eyes)
print(Girl1.ears)