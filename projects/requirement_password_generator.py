import random

print("welcome to the Password Generator".center(100,"-"))

name = str(input("name: "))
symbols = (input("symbols: "))
numbers = int(input("numbers: "))

password = (name+symbols+str(numbers))
print(password)
print(type(password))

final_password = ""
for i in range(len(password)):
    value = random.choice(password)
    final_password += value

print(final_password)

