# #set->mutable(hasable object haru chahi mutable hunxa like tuples , list is not hasable object) values are randomly poisitioned , no indexing,no slicing due to random position
#duplicate value will be removed automatically in set

set1 = {10,True,1,"sara"}

# #to create empty set
# set2 = set() #set2={} this is dict
# print(set1)
# print(type(set1))
# print(set2)
# print(type(set2))

# #to add element in set
# set1.add(22)
# print(set1)

#to add multiple element 
# set1.update([22,23,24]) #list ko value matrai chahi pass garna milyo
# print(set1)

#remove an element -> if element is not present it will thorugh an error
# set1.remove(100)
# print(set1)

#discard an element -> if element is not present it will not through any error
# set1.discard(100)
# print(set1)

#to clear element -> creates an empty set
# set1.clear()
# print(set1)

#pop-> removes last element twra in set no position so randomly value pop gardinxa aauta
# set1.pop()
# print(set1)

#tuples can be added but list cannot since it is mutable and unhasable object while sets are hasable and immutable

# set2 = {(1,2,3,4),5,6,"sara",(2,3,4,4)}
# print(set2)

##operations in sets
set3 = {1,2,3,4,5}
set4 = {100,3,4,5,6,7,8}
set5 = {3,2,10,11,12,5}

#union 
# print(set3 | set4)
# print(set3 | set4 | set5) #multiple
# print(set3.union(('mohan','shyam'))) #passing tuples to union
# print(set3 | {1,2,"sara"}) #we cannot do this in tuples but with same type set is possible

#updating value of set3 (Set4 ko sabai value halerw)
# set3.update(set4)
# print(set3)

#intersection
# print(set3 & set4)
# print(set3 & set4 & set5)
# set3.intersection_update(set4) #common item intersection item matrai aauxa set3 ma 
# print(set3) #3,4,5
# print(set4)

#difference
# print(set3-set4)
# print(set4-set3-set5)
# set3.difference_update(set4,set5) #difference wala matrai set3 ma aauxa multiple rakhna milxa set4,set5,set6..
# print(set3)

#symmetric difference
# print(set3 ^ set4)
# print(set3 ^ set4 ^ set5) #pahili set = set3^set4 garxa ani set-set5 sanga 

# set3.symmetric_difference_update(set4)
# print(set3)


# set6 = {1,2,3,4,5}
# set7 = {1,2,3,4,5,6,7,8}
# #disjoint set-> not common aauta pani between sets
# print(set6.isdisjoint(set7)) #false
# print(set6.isdisjoint([6,7])) #true

# #subset -> set1<=set2 (sabai set1 ko value set2 ma hunu parxa)
# print(set6.issubset(set7)) #true

# #superset -> set2<=set1 reverse of subset (sabai set2 ko value set1 ma xa herxa)
# print(set6.issuperset(set7)) #false

# #clear-> empty set
# set6.clear()
# print(set6)

#del-> set variable purai nai delete gardinxa 
# del set6
# print(set6)

##frozen set-> immutable version of set, and unordered like set

# tuple of vowels
# vowels = ('a', 'e', 'i', 'o', 'u')

# fSet = frozenset(vowels)
# print('The frozen set is:', fSet)
# print('The empty frozen set is:', frozenset()) #if no arguement passs empty set yo hunxa

# # frozensets are immutable
# # fSet.add('v')

# #frozen set for dictionary

# person = {'name' : 'sara',
#           'age' : 22}

# frozen1 = frozenset(person)
# print(frozen1)
# print(type(frozen1))

# #error
# # frozen1['school'] = "new summir"
# # print(frozen1)

# #operations of set garna milxa frozenset ma
# # Frozensets
# # initialize A and B
# A = frozenset([1, 2, 3, 4])
# B = frozenset([3, 4, 5, 6])

# # copying a frozenset
# C = A.copy()  # Output: frozenset({1, 2, 3, 4})
# print(C)

# # union
# print(A.union(B))  # Output: frozenset({1, 2, 3, 4, 5, 6})

# # intersection
# print(A.intersection(B))  # Output: frozenset({3, 4})

# # difference
# print(A.difference(B))  # Output: frozenset({1, 2})

# # symmetric_difference
# print(A.symmetric_difference(B))  # Output: frozenset({1, 2, 5, 6})
# # Frozensets
# # initialize A, B and C
# A = frozenset([1, 2, 3, 4])
# B = frozenset([3, 4, 5, 6])
# C = frozenset([5, 6])

# # isdisjoint() method
# print(A.isdisjoint(C))  # Output: True

# # issubset() method
# print(C.issubset(B))  # Output: True

# # issuperset() method
# print(B.issuperset(C))  # Output: True

#error
# D = A.intersection_update(B)
# print(D)
# A.add(5)
# print(A)