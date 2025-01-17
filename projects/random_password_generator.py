import random

print("welcome to the Password Generator".center(100,"-"))

letters = int(input("How many letters would you like in your password?: "))
symbols = int(input("How many symbols would you like in your password?: "))
numbers = int(input("How many letters would you like in your password?: "))
password = ""

#to generate letters
for i in range(0,letters):
    generate_letters = random.choice('abcdefghijklmnopqrstuvwxyz')
    password += generate_letters

#to generate symbols
random_symbols = ['!','#','%','$','(',')','*','+']
symbols1 = ""
for j in range(0,symbols):
    generate_symbols = random.choice(random_symbols)
    password += generate_symbols

#to generate numbers
random_num = ""
for k in range(0,numbers):
    generate_num = random.choice('0123456789')
    password += generate_num


#final password
final_password = ""
for value in range(len(password)):
    total = random.choice(password)
    final_password += total    
print(final_password)