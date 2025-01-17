#types of arguments

#1.positional argument-> arguments rw parameter ko value aautai position ma hunu paryo

# def show (name,age):
#     print(f"my name is {name}")
#     print(f"age is {age}")

# show(20,"sara") #name->20,age-> sara aauxa doesnot make sense
# show("sara",20) #this makes sense and is right

#2.keyword argument -> full defined gardya hunxa argument ma so position different vayeni farak pardaina
# def show (name,age):
#     print(f"my name is {name}")
#     print(f"age is {age}")

# #dubai right hunxa
# show(age = 20,name="sara") 
# show(name="sara",age = 20) 

#3.default argument -> last ma matrai default assign garna milxa

# def show (name,age,address="ktm"): #default value
#     print(f"my name is {name}")
#     print(f"age is {age}")
#     print(f"address is {address}")

# #dubai right hunxa
# # show(age = 20,name="sara") 
# show(name="sara",age = 20,address="butwal") #yesari ya argument ma define garyo vane yahi address linxa not default(override gareko value)
# show(name="sara",age = 20) 

#4.arbitary argument : variable length argument aauta parameter ma multiple argument pass garna milxa ani tuple ko form ma print hunxa
#symbol-> *
# def show(*n):
#     print(n)
#     print(type(n)) #class tuple nai hunxa
# show([1,2,3,4],[1,2,3])
# show(1,2,3)


#5.arbitary keyword argument: only use in key,value wala pair not like dict->key:value, normally chahi key=value
#symbol - **-> key,value

# def show(*a,**n): #*a aagadi nai define hunxa jaile **n vanda
#     for i,j in n.items():
#         print(i,j)
#         print(type(i))
#         print(type(j))
#     print(a)
#     print(type(a))

# # show(name="sara",age=20)
# show(1,2,3,name="sara",age=20)

#arbitary argument more example 
#no global variable accessed by it?? it throwed error
def add(a,*num): 
    c=0
    for i in num:
        print(i)
        c += i
    print("sum: ",c)
    print(a)

add(2,2,3) #bydefault a ko value first position ko hunxa->2



