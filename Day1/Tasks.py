# a = "helloworld"
# print(a[0:5])

# b = "PythonProgramming"
# print(b[13::])

# #For the string "abcdefg", how can you slice the string to get every second character starting from the first?
# string1 = "abcdefg"
# print(string1[::2])

# #How can you reverse the string "Palindrome" using slicing?
# string2 = "Palindrome"
# print(string2[::-1])

# #What will be the result of the slicing operation s[3:] if s = "DataScience"?
# #aScience

# #How would you extract every second character in reverse order from the string "abcdefgh"?
# string3 = "abcdefgh"
# print(string3[7:0:-2])

# #For the string "ArtificialIntelligence", how would you extract the substring "Intelli" using slicing?
# string4 = "ArtificialIntelligence"
# print(string4[10:16])

# #Given two strings str1 = "Hello" and str2 = "World", concatenate them to form a new string "HelloWorld".
# str1="hello"
# str2="world"
# print(str1+str2)

# # Extract the substring "loWor" from the string str = "HelloWorld" using slicing.
# str = "HelloWorld"
# print(str[3:8])

# # Convert the string str = "apple,banana,cherry" to a list of fruits.
# str = "apple,banana,cherry"
# print(str.split(","))

#6)a="my name is rita" use all method of string give
a="my naMe is ritam"

print(a.capitalize())
print(a.count('m'))
print(a.center(30,"&"))
print(a.find('a'))
print(a.islower())
print(a.split(" "))
print(a.strip('m'))
print(a.rstrip('m'))
print(a.lstrip('m'))
print(a.replace("rita","sara"))
print(a.swapcase())
print(a.upper())
print(a.title())

#Given two strings str1 = "Hello" and str2 = "World", concatenate them with a space in between and print the result.(i.e=adding)

str1 = "Hello" 
str2 = "World"
print(str1+" "+str2)

#Given a string str = "PythonProgramming", find and print the length of the string.
str = "PythonProgramming"
print(len(str))

#)Given a string str = "HelloWorld", extract and print the substring "World" using slicing
str = "HelloWorld"
print(str[5::])

#Convert the string str = "python" to uppercase and print the result.
str = "python"
print(str.upper())

#Convert the string str = "PYTHON" to lowercase and print the result.
str = "PYTHON"
print(str.lower())

#Reverse the string str = "Python" and print the result.
str = "Python"
print(str[::-1])