a = [1,2,3,4,5]
b = []
#longmethod
# for i in a :
#     b.append(i+2)
# print(b)

#shorcut type ko short hand
# [b.append(i+2) for i in a]
# print(b)

# name = "sara"
# c=[]
# [c.append(i+'a') for i in name]
# print(c)

#length 
# a = ["sita","hari","ram","shyam"]
# b = len(a)

# values = []
# for i in a:
#     value = len(i)
#     values.append(value)
#     print(f"{i}:{len(i)}")
# print(values)

# values = [f"{len(i)}:{i}" for i in a]
# print(values)



b = ["youtube.com","facebook.com","whatsapp.com","ram.com"]

# for i in b:
#     values = i.strip(".com")

values = [i.removesuffix(".com") for i in b]
print(values)