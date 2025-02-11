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

b1 = B()
#     print(b1._name)
#     b1._show()
b1.show()
# showdata()

##public method to access private
a1 = A()
a1.show2()