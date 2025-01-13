#repeating over and over
#only two types of loop : for and while loop

#range(start,end,steps) -> end value will never come only one less than end value will come
# a = range(10)
# print(a)

# for b in range(0,10,1):
#     print(b)

#forloop

# for i in range(10):
#     print(i,end=" ") #end-> line break huna didaina so horizontally print hunxa

# for i in range (7,0,-1):
#     print(i)
#     if i==3:
#         print("go")

#loop in list
# list1 = ['ram','hari','sita','rita']

# for i in list1:
#     print(i,end=" ")


#harek index print garxa
# i = "sita"

# for var in i:
#     print(var)

# list1 = ['ram','hari','sita','rita']

# for i in list1:
#     print(i)

# for i in list1:
#     for j in i:
#         print(j)

#multiply 

# for i in range(1,11):    
#     print(f"2 x {i} = {2*i}")

#list in loop
# numbers = [2,3,4,5]
# num2 = []
# for i in numbers:
#     num = i**2
#     num2.append(num)
# print(f"list: {num2}")

#tuples in loop -> its immutable so need to convert list to tuple
# numbers = (2,3,4,5)
# num2 = ()
# num3 = []
# print(type(num2))
# for i in numbers:
#     num = i**2
#     num3.append(num)
#     num2 =  tuple(num3) 
# print(f"list: {num2}")

#sets in loop
# numbers = {2,3,4,5}
# num2 = set()
# for i in numbers:
#     num = i**2
#     num2.add(num)
# print(f"sets: {num2}")

#dict in loop
# numbers = { 'name': 'sara', 'age':22, 'address':'shantinagar' }
# num2 = {}
# for key in numbers:
#     # print(numbers[key])
#     num2[key] =  numbers[key] #dynamic pL ho python so num2[key] tesari lekhne bitikai automatic add hunxa num2 ma key value bujxa python lae
# print(num2)

