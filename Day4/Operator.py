#operator= symbol that perform operation

#1. arithmetic operator(+,-<,/)

# num1 = 13
# num2 = 2

# #addition
# print(num1+num2)

# #subtraction
# print(num1-num2)

# #multiplication
# print(num1*num2)

# #division
# print(num1/num2)

# #modulus
# print(num1%num2)

# #floor 
# print(num1//num2)

# #power
# print(num1**num2)

# #2.Relation/comparison operator(<,>,==,<=,>=,!=)
# a = 12
# b = 15

# print(a<b)
# print(a>b)
# print(a==b)
# print(a<=b)
# print(a>=b)
# print(a!=b)

# #3.assignment operator(=,+=,-=,//=,*=,**=)

# a = 4
# a += 1
# a += 2
# print(a)
# a -= 2

#4. logical operator (and,or,not)
# a = True
# b = False
# print(a and b)
# print(a or b)
# print(not(a))

#5. membership operator(in,not in)
# in -> only string
# a = "my name"
# b = 15
# print("my" in a)
# print("my" not in a)

#6. identity operator -> memory address hererw equal xa ki xaina vanxa (int=5 xa ani a,b,c sabai value lae aauta lai point garxa integer,float ko case ma)
# a = [1,2,3]
# b = [1,2,3]
a = 5.2
b = 5.2
print(id(a)) 
print(id(b))
print(a is b)
print(a==b) #value matrai herxa
# print(15 is not b)



#7. bit wise operator-> binary operation hunxa 12-> 1101 , 15-> 1111

# and operator -> & (both true-> true, both false-> false, onefonet,onetonef-> false)
# a = 20
# b = 15
# print(a & b) #1101+1111

# #or operator -> | (one true-> true, both true-> true , both false-> false)
# print(a | b)

# #negotation operator (~) -> 2's complement garxa
# print(~(a)) #20-> -21, #13-> -14

# #xor
# #different-> true , same-> false
# print(a ^ b)


