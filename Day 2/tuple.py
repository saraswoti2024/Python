#immutable ->original value change hudaina
#faster performance in comparsion with list

# a = (23,46.5,"hello",23,32)

# #type
# print(type(a))

# #length
# print(len(a))

# #individual type
# print(type(a[2]))
# print(a)

# #negative indexing starts from -1 (ending)
# print(a[-2])

# #positive indexing starts from 0(starting)
# print(a[0])

# #slicing in tuple-> same as we did in string 
# print(a[1:4])
# print(a[::2])

#nesting of tuples
tuple1 = (0,1,2,"sara",True)
tuple2 = (2,3,"lax",11,111,11.11,"parru")
tuple3 = (tuple1,tuple2,5,6,"saraswoti")
# print(tuple3)
# print(tuple3[1][0:5])
# print(tuple3[1][4:1:-1])

#concatenation of tuples
tuple3 = tuple1 + tuple2 #sabai ya vitrw vako tuples lai yeslae linxa
print(tuple3)
print(len(tuple3)) #12

tuple4 = (12,2,34,5,6) *3 #3 times printing
print(min(tuple4))
print(sorted(tuple4))
print(tuple1.count(True))

#list to tuple convert
list1 = [1,2,3]
list2 = tuple(list1)
print(type(list2))
print(tuple4)

#converting tuples to list
print(list(tuple4))

tupleconvert = list(tuple4)
print(tupleconvert)
print(type(tupleconvert))