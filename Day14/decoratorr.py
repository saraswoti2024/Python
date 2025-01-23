#@-> decorator
#function that takes another function arguments and add some features and return it to new function
#kai new feature add garnu parxa vane new function banauxam ani old sanga merge garxam
#example: login ,logout page is needed in everypages so a different function containing that code is made and added to all pages functions

def outer(a):
    def inner():
        print("i am inner")
        a()
    print("i am outer")
    return inner

@outer
def show():
    print("i am outside")
show()

