##dict is mutable

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


#removing using pop
# person = {'name': 'Sarah',
#            'age': 35, 
#            'city': 'Miami', 
#            'job': 'Lawyer'}
# person.pop('age')
# person.clear()
# print(person)

#using del to delete the dict purai nai
# del person
# print(person)

