#1.bytes-> immutable range(0,255)
a = bytes([1,2,3,4,5])
print(type(a))
print(a)

#error aauxa since it is immutable
# a[1] = 10
# print(a)

#2.bytearray-> mutable range(0,255)
# a = bytearray([1,2,15,4,6,298]) #error since 298 is not in the range
a = bytearray([1,2,255])
print(a)
a[1] = 7
a[0] = 128
print(a)
