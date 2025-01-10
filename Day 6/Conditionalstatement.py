import random
#if statement
# a = 11
# if(a>12):
#     print("a is greater")
# else:
#     print("a is smaller")


#if,elif,else statement
# a = "welcome to our bus"
# print(a.center(80,"*"))

# age = int(input("Your age: "))

# if age<=12:
#     print("you have to pay Rs.20")
# elif age>12 and age<=18:
#     print("you have to pay Rs.40")
# elif age>18 and age<=40:
#     print("you have to pay Rs.80")
# else:
#     print("you have to pay Rs.100")

#calculator app
# print(("calculator").center(80,"*"))

# num1 = float(input("Enter num1: "))
# operator = input("Enter operator: ")
# num2 = float(input("Enter num2: "))

# if operator=='+':
#     print(f"{num1} + {num2} = {num1+num2}")

# elif operator=='-':
#      print(f"{num1} - {num2} = {num1-num2}")

# elif operator=='*':
#      print(f"{num1} * {num2} = {num1*num2}")

# elif operator=='/':
#     a=num1/num2
#     print(f"{num1} / {num2} = {num1/num2:.2f}")
    
# elif operator=='%':
#      print(f"{num1} % {num2} = {num1%num2}")
# else:
#      print("provide a valid operator")
    
#rock,paper,scissor game

# print(("rock,paper,scissor game").center(80,"*"))

# user = (input("Enter your choice:")).upper()
# computer = random.choice(['S','P','R'])

# print(user)
# print(computer)

# if((user=='R' and computer=='S') or (user=='S' and computer=='P') or (user=='P' and computer=='R')):
#     print("User Won")

# elif(user not in ['S','R','P']):
#     print("Invalid,please try again")

# elif(user==computer):
#     print("draw!")

# else:
#     print("User Lose and Computer Won")

#short hand -> only used in one if
a = 5
b = 3
if a>2: print("a is greater")
print("a is greater") if (a>b) else print("a is smaller")



