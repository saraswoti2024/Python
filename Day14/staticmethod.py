##methods that dont use self parameter
##self parameter is used in objects to call store
##works at class level

#static method-> aauta default self parameter hunai parxa class vitrw ko value call garna so staticmethod use garyo vanae chahi parena works as both cls,self default

#__init__ wala ma chahi hudaina kna vanae tya hamle attribute define garya hoo
class A:
    name = "saraswoti"

    @staticmethod
    def initialize_age(age):
        print(f"Age initialized to: {age}")

    @staticmethod
    def show(a, b):
        print(a + b)

# Use the static methods directly from the class
A.initialize_age(22)  # This will print "Age initialized to: 22"
A.show(2, 3)          # This will print "5"
