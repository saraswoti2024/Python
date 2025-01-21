# Write a recursive function to compute the factorial of a given number 
# 𝑛
# factorial(5)=120.

# def fact(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*fact(n-1)
    
# n = 5
# print(fact(n))

#Write a recursive function that calculates the sum of the digits of a given integer.


# def fact(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         for i in len(n):
#             return i+fact(i)
    
# n = 234
# print(fact(n))

#series of fibonacci
#0,1,1,2,3,5,8,13
# a = 0 
# b = 1
# c = a+b 
# d = c+b

#Create a function  that takes two numbers as input and returns their sum.

# def sum(a,b):
#     return a+b

# print(f"sum: {sum(2,3)}")

#Write a function factorial that computes the factorial of a number using recursion.

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)

# n = 5
# print(fact(n))

#Define a function  that checks whether a given string is a palindrome.

# def func_palindrome(name):
#     reverse = name[::-1]
#     # print(reverse)
#     if(name==reverse):
#         return "palindrome"
#     else:
#         return "not palindrome"
    
# name = "aabaa" 
# print(func_palindrome(name))

#Write a function max_of_three that takes three numbers and returns the largest of the three.


# def max_of_three(num1,num2,num3):
#     # value = max([num1,num2,num3])
#     if num1>num2 and num1>num3:
#         return num1
#     elif num2>num3 and num2>num1:
#         return num2
#     else:
#         return num3

# a = 4
# b = 2 
# c = 20
# values = max_of_three(a,b,c)
# if values ==a:
#     print("a is greater")
# elif values ==b:
#     print("b is greater")
# else:
#     print("c is greater")

#Create a function that takes a number as input and returns True if the number is prime, otherwise False.


# def primecheck(number):
#     is_prime = True
#     for i in range(2,number):
#         if number%i==0:
#             is_prime = False

#     if(is_prime==True):
#         print("is prime")
#     elif(is_prime==False):
#         print("is not prime")    

# number = int(input("Enter num: "))
# primecheck(number=number)

#Write a function fibonacci that takes a number n and returns the first n terms of the Fibonacci sequence as a list.
# def fibonacci(number):
#     num2 = []
#     num1 = [0,1]
#     for i in range(0,number):
#         num2 = num1[i] + num1[i+1]
#         num1.append(num2)
#     print(num1)
    
# number = 8 #0112358
# fibonacci(number)

#Define a function count_vowels that takes a string as input and counts the number of vowels in the string.

# def count_vowels(value2):
#     count = 0
#     vowels = "aeiouAEIOU"
#     for i in value2:
#         if i in vowels:
#            print(i)
#            count += 1
#     print("total is : ",count)
            
# value = "qqeeuaaeinou"
# value2 = list(value)
# print(value2)

# count_vowels(value2)

# Write a function  that takes a list and returns a new list with duplicates removed.

# def duplicate_removed(list1):
#     list2 = set(list1)

#     return list(list2)

# list1 = [1,2,"sara",2,"sara",5]
# print("removing duplicate:",duplicate_removed(list1))


# Write a function  that takes a string and returns the reversed string.

# def reverse_string(value):
#     value_reversed = value[::-1]
#     return value_reversed


# string_Value = input("enter a word: ")
# print(f"reversed value: {reverse_string(string_Value)}")

# Write a function sort_list that takes a list of numbers and returns the list sorted in ascending order.

# def sort_list(num_list):
#     valuenew = []
#     for num in num_list:
#          value = int(num.strip())
#          valuenew.append(value)

#     valuenew.sort()  
#     print(valuenew)

#     valuenew.sort(reverse=True) 
#     print(valuenew)

# num_list = (input("enter number using comma: "))
# newvalue = num_list.split(",")
# print(newvalue)
# sort_list(newvalue)