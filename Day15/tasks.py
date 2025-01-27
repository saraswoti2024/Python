#1.

# class account:
#     balance = 20000
#     account_no = 1234353345

#     def debit(self,amount):
#         self.balance += amount
#         print(self.balance)
    
#     def credit(self,amount):
#         self.balance -= amount
#         print(self.balance)

# account1 = account()
# account1.debit(1000)
# account1.credit(200)

#2.

class circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        print(2*self.pi*self.radius)
    
    def circumference(self):
        print(self.pi*(self.radius**2))

circle1 = circle(5)
circle1.area()
circle1.circumference()


