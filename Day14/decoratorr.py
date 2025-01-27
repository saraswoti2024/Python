#@-> decorator
#function that takes another function arguments and add some features and return it to new function
#kai new feature add garnu parxa vane new function banauxam ani old sanga merge garxam
#example: login ,logout page is needed in everypages so a different function containing that code is made and added to all pages functions


#suppose login page
# def outer(a):
#     def inner():
#         print("i am inner")
#         a()
#     print("i am outer")
#     return inner

# #suppose homepage
# @outer
# def show():
#     print("i am outside")
# show()


#with explanation

# The show function is defined.
# The outer function is called with show as its argument (outer(show)).
# The outer function prints "i am outer" and returns the inner function.
# The returned inner function is assigned back to the show variable. now the show variable is inner()
# After the decorator application, the show variable now refers to the inner function returned by outer. Here's what happens when you call show():
# The inner function (now referred to by show) is called.
# Inside inner, it prints "i am inner".
# Then, inner calls the function a(), which is the original show function passed as an argument to outer.
# The original show function prints "i am outside".

# def outer(a):#3
#     def inner(): #9
#         print("i am inner") #10
#         a() #11
#     print("i am outer") #4
#     return inner #5

# def show():
#     print("i am outside") #12

# print("Before decorator:", show) #1
# show = outer(show) #2 #6 # This is what @outer does
# print("After decorator:", show) #7

# show() #8  # This will call the inner function

