#Write a program that asks the user to enter a number and checks whether the number is odd or even

# number = int(input("Enter a number: "))

# if(number%2)==0:
#     print("Number is Even")
# else:
#     print("Number is odd")

#Write a program that takes a score as input and assigns a grade based on the following criteria:
#90 and above: Grade A
# 80–89: Grade B
# 70–79: Grade C
# Below 70: Grade

# score = float(input("Enter your score: "))

# if(score>=90 and score<=100):
#         print("Grade A")
# elif(score>=80 and score<=89):
#         print("Grade B")
# elif(score>=70 and score<=79):
#         print("Grade C")
# elif(score<70 and score>=0):
#         print("Grade D")
# else:
#         print("Enter a valid number from 0-100")

#Write a program to check if a person is eligible to vote. The eligibility age is 18 or above.

# age = int(input("your age: "))

# if(age>=18):
#     print("you're eligible to vote")
# else:
#     print("you're not eligible to vote")

#Write a program that takes three numbers as input and prints the largest among them.

# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# num3 = int(input("Enter num3: "))

# if(num1>num2 and num1>num3):
#     print("num1 is greatest")

# elif(num2>num1 and num2>num3):
#     print("num2 is greatest")

# elif(num3>num1 and num3>num2):
#     print("num3 is greatest")


#Write a program to check if a given year is a leap year or not. A year is a leap year if:It is divisible by 4 but not divisible by 100, OR It is divisible by 40

# year = int(input("year: "))

# if(year%4==0 and year%100!=0):
#     print("year is a leap year")
# else:
#     print("not a leap year")

#
# If a number is divisible by 3, print "Fizz".
# If divisible by 5, print "Buzz".
# If divisible by both, print "FizzBuzz".
# Otherwise, print the number itself

# num = int(input("enter a number: "))

# if (num%3==0 and num%5==0):
#     print("FizzBuzz")

# elif num%3==0:
#     print("Fizz")

# elif num%5==0:
#     print("Buzz")

# else:
#     print(f"{num}")


# Given two variables x = 15 and y = 20, use conditional statements to print which variable is larger, or if they are equal.

# x= 20
# y = 20

# if(x>y):
#     print("x is greater")
# elif(x<y):
#     print("y is greater")
# elif(x==y):
#     print("x is equal to y")

#  Given a variable num = 7, use a conditional statement to check if the number is even or odd and print the result. 

# num=12

# if(num%2==0):
#     print(f"even: {num}")
# else:
#     print(f"odd: {num}")

#Check if the value 10 is not present in the tuple t = (5, 15, 20, 25).

# t = (5,15,20,25)

# if(10 not in t):
#     print("not present")
# else:
#     print("present")
    
# Determine if the value 25 is present in the list lst = [10, 20, 30, 40, 50] using a simple conditional statement
# lst = [10, 20, 30, 40, 50]

# if(25 in lst):print("present")
# else: print("not present")

# Check if the value 100 exists in the set s = {50, 75, 100, 125}.
# s = {50,75,100,125}
# if(100 in s): print("present")
# else: print("not present")

#bmi calculator

# weight = float(input("enter your weight in kg: "))
# height = float(input("Enter your height in meter: "))

# bmi = weight / height**2
# print(int(bmi))

#nested if,ifelse,elif
#exercise bmi

# year = int(input("Enter year: "))

# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("Leap Year")
#         else:
#             print("not a leap year")
#     else:
#         print("leap year")
# else:
#     print("not a leap year")

#who pay the bill task
# import random
# names = input("Enter names seperated by comma: ")
# name_lists = names.split(",")

# res = random.choice(name_lists)
# print(f"{res} will pay the bill")
