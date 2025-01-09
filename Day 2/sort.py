#sort -> original list mai change gardinxa,method ho
#sorted -> original list ma change gardaina

# ascending
a = [6,5,2,1,3,4]
a.sort()
c = a.sort()
print(c)
print(a)

b = sorted(a)
print(b)

#descending
a.sort(reverse=True)
print(a)

b = sorted(a,reverse=True)
print(b)
