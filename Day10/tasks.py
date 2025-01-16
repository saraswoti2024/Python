#Write a program to create a function that takes two arguments, name and age, and print their value.

# def value(name,age):
#     print(f"{name},{age}")

# value("sara",22)

#Write a program to create function func1() to accept a variable length of arguments and print their value.

# def func1(*n):
#     print(n)

# func1(1,2,3,"sara",4,"paru")

#Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction.

# def calculation(num1,num2):
#         print(num1+num2)
#         print(num1-num2)

# num1 = 2
# num2 = 5
# (calculation(num1,num2))

#Write a program to create a function show_employee() using the following conditions.

# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

# def show_employee(name,salary=9000):
#     print(f"name: {name}")
#     print(f"salary: {salary}")

# show_employee("saraswoti",1000)

#Create an outer function that will accept two parameters, a and b

# a = 2 
# b = 3

# def func():
#     print(a)
#     print(b)

# func()


#Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it

# def func1():
#     b = func2(2,3)
#     return 5 + b

# def func2(a,b):
#     return a+b

# print(func1())

# def func1(a,b):
#     def func2(a,b):
#         return a+b
#     add = func2(a,b)
#     return add+5

# print(func1(2,8))
