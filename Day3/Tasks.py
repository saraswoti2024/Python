#sets
s1 = {20,30,40,50}

#adding element 
s1.add(60)
print(s1)

#removing element
s1.remove(20)
print(s1)

#checking if element 30 is in the set
print(30 in s1)

#length of set
print(len(s1))

s2 = {5,6,7,8,9}
s3 = {7,8,9,10,11}

#union 
print(s2 | s3)

#intersection
print(s2 & s3)

#different between
print(s2-s3)

#symmetric difference
print(s2 ^ s3)

#check if subset
print(s2.issubset(s3))

#check if superset
print(s2.issuperset(s3))

#check if disjoint
print(s2.isdisjoint(s3))


##dict task

#1 #2
person1 = {
    'name' : 'Bob',
    'Age' : 30,
    'city' : 'Los Angeles',
    'job' : 'Doctor',
    'Email': 'sara@gmail.com'
    }
print(person1['name'],person1['job'])

#3
person2 = {
    'name' : 'John',
    'Age'  : 28,
    'city' : 'chicago' 
}

#adding a new key-value pair
person2['job'] = "Teacher"
print(person2)


#updating value
person2['Age'] = 29
print(person2)

print(person1.update(person2))

#nested dictionary
person3 = {
    'fruits' : {'fruit1' : 'Apple',
                'fruit2' : 'orange',
                'fruit3': 'pineapple'},
    'name' : {
            'name1' : 'sara',
            'name2' : 'paru',
            'name3' : 'lakxh',
            'name4' : 'Ram',
                            },
    'email' : 'saraswoti@gmail.com',
    'number' : 984353535,
    'age' : 22,
}
print(person3['name']['name1'])
person3['name']['name1'] = "saraswoti"
print(person3)

#find common keys between two dictionaries -> values chahi common dekhaunae hudaina only keys
print(person1.keys() & person2.keys()) 

#removing key-value pair
person = {'name': 'Sarah',
           'age': 35, 
           'city': 'Miami', 
           'job': 'Lawyer'}

