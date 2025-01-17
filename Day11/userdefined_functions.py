#4 types of functions

#a. no arguments and no return value
# def greet():
#     print("saras")

# greet()
# greet()
# greet()



#b.with arguments and with return value
def greet(name):
    name1 = 'sara'
    name = name1
    return name

print(greet('saraswoti'))

#c.without arguments and with return value
def add():
    a = 2
    b = 7
    return a+b

print("num is",add())

#d.with arguments and no return value
def add(a,b):
    print(a+b)

add(2,3)
