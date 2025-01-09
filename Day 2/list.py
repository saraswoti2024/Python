# # #list is muttable means original value can changed
# # #different data types can be stored

# l1 = ['sara',12,12.23,True,"saraswoti",6+3j]
# print(l1)

# #append-> to add new element in a list 
# # l1.append("banana")
# # print(l1)

# # #extend-> to add multiple elements in a list
# # l1.extend(['saru','laxman',143,143.2])
# # print(l1)

# #insert-> to add in specific index
# l1.insert(2,"bimala") #(index 2, new_Value->bimala)
# print(l1)
# #to access first bata
# print(l1[0])

# #to access last bata
# print(l1[-1])
# print(l1[-3])

# #to reverse an element in a list
# print(l1[::-1])
# l1.reverse()
# print(l1)

# #to print length
# print(len(l1))

# #slicing in list
# print(l1[1:4])

# #sorting the list-> same data type only sorting
# l2 = [13,2,1,4]
# l3 = ['sara','lakx','paru']
# l2.sort()
# print(l2)

# l3.sort()
# print(l3)

# #max,min value-> same data type only
# print(max(l2))
# print(min(l2))

# #to remove 
# l1.remove("saraswoti")
# print(l1)

# #pop-> last elemnt remove garxa
# print(l1.pop())

#nested list 
list1 = [[2,"sara",3,4,5,6,7,8,9],4,5,["saru",10,11.23,11.11]]
print(len(list1))
print(list1)
print(list1[0][2])
print(list1[3][5:1:-1])
print(list1[-1])
 
#yesari ni milxa
list2 = [list1,3,2,3]
print(list2)

#converting list to set
c = [1,2,4]
b= set(c)
print(type(b))
print(b)