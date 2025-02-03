##private(like) atrributes and modules
##private method intialize-> __variable_nameormethodname


class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello")
        print(self.__name)

    def acessingprivate(self):
        self.__hello() 

p1 = Person()
#print(p1.__name) ##throws error coz its private
# p1.hello() ##same here coz its private
p1.acessingprivate() #this works calling from private to public
