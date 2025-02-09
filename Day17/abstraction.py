##with help of abc(abstract base classes) module we can achieve abstraction , we need to import ABC class from abc module

##abstract class-> kunai class xa ani tesko object banauna restrict garna ko lagi use garxa 
##aauta abstract class ma aauta abstract method hunai parxa(abstract method ma kailae ni kai print haru testo kai hunna simple pass matra hunxa)
from abc import ABC,abstractmethod

class Vehicle(ABC): ##abstract class can have multiple methods
    def __init__(self,n):
        self.n = n
    
    @abstractmethod  ##object banauna didaina 
    def show(self):
        pass
    ###dubai abstract class rw method vako hunu parxa object nabanna ko lagi , abstract class xa ani method xaina vanae hudaina same as abstract method xa class xaina vanae hudaina

    def display(self): ##normal method is also known as concrete method
        print("i can display in vehicle if there is no abstractmethod decorator")

v = Vehicle(2)
v.show()
v.display()