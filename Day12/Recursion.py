#recursion->function calling itself(function inside function)
# base condtion: 1000 choti limit hunxa func call garirakhnae
#to find factorial 
# def factorial(num):
#     if num==1 or num==0:
#         return 1
#     else:
#         return (num* factorial(num-1)) #factorial() function call vairakhxa until it is 1 ani num ko value sanga multiply ni vairaxa

# num = 5
# print("factorial is : ",factorial(num))


#my logic->same as above
# Write a program to calculate the factorial of a number using recursion.

# The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
# For example, for input 5, the return value should be 120 because 1*2*3*4*5 is 120.

# def factorial(num):
#     if num==1 or num==0:
#         return 1
#     for i in (num,1,-1):
#         print(i)
#         return i*factorial(num-1) #5*4*3*2*1 = 120

# num = 5
# print("fact is: ",factorial(num))

##example
#stack form 3,2,1,0 ani return hunxa mathi bata tala 1,2,3
#0 
#1-1
#2-2
#3-3
def display(n):
    if(n<1):
        return n
    else:
        print(n)
        display(n-1)
        print(n)

n = 3
print(display(n))


