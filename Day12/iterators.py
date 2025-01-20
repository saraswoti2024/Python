from functools import reduce
# map function

num = [1,2,3,4]
# for i in num:
#     print(i*2)

#normally function vitrw value return garerw list ko sabai value ekaichoti kai operation perform garda(like *,-,+) error dekhauxa ,example down below so we use map function
# def value(num):
#     for i in num:
#         print(i*2)

# value2 = value(num)
# # print(value2)

##map function
# n = [1,2,3,4]

# def value(n):
#         return n*2

# value2 = list(map(value,n))
# print(value2)
# # print(value(n))

# #lambda function
# value2 = list(map(lambda a:a*2,n))
# print(value2)

# #converting to upper case
# fruits = ['apple', 'banana', 'cherry']
# res = map(str.upper, fruits)
# print(list(res))

#filter function
n = [1,2,3,4,5,6,8,10,19,18]

# def value(n):
#         if n%2==0:
#          return n
        
# value2 = list(filter(value,n))
# print(value2)
# # print(value(n))

#using lambda
value2 = list(filter(lambda a: a%2==0,n))
print(value2)

#reduce function(function,value)-> dui dui oota value lidai operation garxa(add,sub,mul) and aarko sanga add garxa c-> a,b (+) then c+d and so on 

def sum(a,b):
    return a+b

print(reduce(sum,n))


#lambda 
sum = reduce(lambda a,b:a+b,n)
print(sum)