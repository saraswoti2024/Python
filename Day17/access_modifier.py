##public : available to every classes,objects
##protected: avaialbe to inherited classes
##private : only avaialble to that class

class A:
    def __init__(self):
        self.age = 22
        self._name = "saraswoti"
        self.__name1 = "parbati"
    
    #protected method
    def _show(self):
        print(f"protected: {self._name}")
    
    ##private method
    def __show(self):
        print(f"private: {self.__name1}, protected: {self._name}")
    
    def show2(self):
        self.__show()


class B(A):
    def show(self):
        self.show2() ##yo garda show hunxa private of inherited A
        # print(f"private of A: {self.__name1}, protected of A: {self._name}") ##private will not be displayed

##protected kai class
A1 = A()
# print(A1._name)
# A1._show()

##private so will not print
# print(A1.__name1) 
# A1.show()

#using different class to call protected vako class

# b1 = B()
# #     print(b1._name)
# #     b1._show()
# b1.show()
# # showdata()

##1.accessing private methods, attributes

##public method to access private(calling private method in public method of same class and calling public method of that class from outside)
# a1 = A()
# a1.show2()

##name mangling , aagadi objectname._classname__privatefunc()
a1 = A()
a1._A__show() ##private method
print(a1._A__name1) #private attribute

##getter and  setter method
#in encapsulation file 
##we use this method to access private datas aaru chahi concept ko lagi matra padheko jasto ho
