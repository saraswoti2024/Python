##main reason to use ducktyping is to support dynamic typing(tahi data type rakhnu pardaina direct python lae thapauxa , c,c++ static vayo tahi ho same concept)

##class matter gardaina k pass garya xam tahi matra matter garxa 
# class of the objects can change as along as the methods are defined on that objects

class Duck:
    def swim(self):
        print("i can swim , i am duck")
    def speak(self):
        print("i can speak,  i am duck")

class Dog:
     def swim(self):
        print("i can swim , i am dog")
     def speak(self):
        print("i can speak,  i am dog")

class Person:
    def speak(self):
        print("i can talk, i am person")

#yeslai class vitrw rakherw ni garna milxa
# def display(namee):
#     namee.swim()
#     namee.speak()
#     print("i am display")

class show:
    def display(self,namee):
     namee.swim()
     namee.speak()
     print("i am display")

show1 = show()
duck1 = Duck()
show1.display(duck1)

# p1 = Person()
# display(p1) ##error will come coz the class person has no method name swim, object class can be different but all the methods that is in display function should be in that class as well .hence this is called ducktyping


    







