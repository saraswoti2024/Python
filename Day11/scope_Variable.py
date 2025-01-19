########local and global variables###############

# a = 10  #global scope-> we cannot modify a global variable inside local variable directly

# def var():
#     # a = a+1 #this will throw error
#     # a=11 #local scope
#     print(a)
# var()

# a=a+2 #this will not throw error
# print(a)

#####global keyword#########################
###to modify variable inside local scopes global keyword is used.
##from local scope we can create global scope as well

# # a = 10  
# global a
# a = 2

# def show():
#     # global a
#     # a = 50
#     print("nested local scope: ",a+5)
#     return a+5

# def var():
#     # global a #this value can be used outside local scope pani
#     a = 20
#     print("inside local scope: ",a)
#     value = show()
#     print("returned value local scope:",value+a)
    
# var()

# a = a+20
# print("outside local scope: ",a)

## global keyword > global variable
name="Jenny's"

def display():
    global name
    name=name+" Lectures"

print(name) #global scope ko value liyo
display() #globally same name define ani modify garya xam so aaba tyo value linxa
print(name) # global keyword use gareko new value liyo
value = name 
print(value) #yesle ni tahi liyo