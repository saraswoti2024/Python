##dict is mutable keys are immutable only values are mutable

# dicts = {}
# print(dicts)
# print(type(dicts))

# d1 = {
#     'name' : 'saraswoti',
#     'age' : 22,
#     'address' : 'Gothatar',
#     'email' : 'saraswotikhadka2k2@gmail.com',
# }
# print(d1)
# print(d1['name'],d1['age'])

# d1['salary'] = 10000
# print(d1)

# del d1['age']
# print(d1)

#value dinxa key name ko
# print(d1.get('name'))

#slicing in dict
# d2={
#     'name' : 'saraswoti',
#     'age' : 22,
#     'marks' : [10,20,30,40,50]
# }
# print(d2)
# print(d2['marks'][0:3])

#removing key-value pair
# print(d2.pop('name'))
# print(d2)

#clearing all value of dict and created empty dict
# print(d2.clear())

#converting list to dict
# l1 = [('name','sara'),('age',22)]
# print(l1[0])
# l2 = dict(l1)
# print(l2)
# print(type(l2))

#nested dictionary
# d1 = {
#     'emp' : {'name' : 'sara',
#              'age' : 50},

#     'emp2' : {'age' : 50},
#     'emp3' : 22,
# }
# d1['emp']['name'] = "saraswoti"
# print(d1)
# print(d1['emp']['age'])

#for multiple deleting,popping key-value use loop
#removing using pop
# person = {'name': 'Sarah',
#            'age': 35, 
#            'city': 'Miami', 
#            'job': 'Lawyer'}

# #adding list values
# person['numbers'] = {123,345,"sara"}

# #nested loop adding bahirw bata
# person['fruits']= {'name':5,'banana':3,'mango':10}

# # person.pop('age')
# person.pop('name')
# person['fruits'].pop('mango') #for nested key-value pop
# # person.clear() #empty hunxa purai dict
# print(person)
# print(person['fruits']['name'])


# #using del to delete the dict purai nai
# # del person #person variable purai nai delete hunxa undefined
# # print(person)
# #single key-value delete garxa(same kaam of pop and yesari delete)
# del person['age']
# del person['fruits']['name']
# print(person)

#using num as key
# data = {
#     1: 'sara',
#     2: 'paru',
#     3: 'luxx',
# }
# print(data[1]) #1 is key here

# #accesing key,value,both
# print(data.keys())
# print(data.values())
# print(data.items()) #type->dict #forbothkeyandvalue access

#using loop

# for i in data:
#     print(i)
#     print(data[i])

# for i in data.items():
    # print(i)

#to copy one dict to another
# data2 = data.copy() 
# #or normally data2 = data (assign garda ni hunxa)
# print(data2)
# print(data)