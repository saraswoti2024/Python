str1 = "Hello"
str2 = "world"
str3 = str1+str2
print(str3)

print(str3[3:8:1])
my_list = [10,20,30,40,50]
third_element = my_list[2]
print(third_element)
mylist = my_list[0:3]
print(mylist)

#5
str = "apple,banana,cherry"

#6
my_list = [1,2,3]
new_list = [1,2,3]*3
print(new_list)

#7
values = ["hello",45,67,89,90,45,45,"apple","orange"]
values.append(34)
print(values)

values.extend([36,"hi",23]) #multiple values add
print(values)

print(values[7][0:3])

values.remove(45)
print(values)

values.clear()
print(values)

a1 = [22,34,"sara",36]
a2 = [34,23,"hi","bye"]
a3 = a1+a2
print(a3)