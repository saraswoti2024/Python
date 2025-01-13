#Write a program to print the squares of numbers from 1 to 10 using a for loop

# for i in range(1,11):
#     print(f"{i}^2 = {i**2}")


#Write a program to print all even numbers between 1 and 20 using a for loop..

# for i in range(1,21):
#     if i%2==0:
#         print(i)

#Write a program to calculate the sum of numbers from 1 to 50 using a for loop

# sum = 0
# for i in range(1,51):
#     sum += i
# print(f"sum of 1 to 50: {sum}")

#Write a program to calculate the sum of all odd numbers between 1 and 100 using a for loop.

# sum = 0

# for i in range(1,101,1):
#     if i%2!=0:
#         sum += i
# print(f"sum of odd number is: {sum}")

#Write a program to find the largest number in a list [2, 8, 1, 16, 5, 23, 7] using a for loop

# list = [2, 8, 1, 16, 5, 23, 7] 
# largest = list[0]
# smallest = list[0]

# # for i in list:
# #     if(largest<i):
# #         largest=i
# # print(largest)

# for i in list:
#     if(smallest>i):
#         smallest = i
# print(smallest)

#prime number

for num in range(2,51):
    for j in range(2,num):
        if(num%j==0):
            break
    else:
        print(num)










       