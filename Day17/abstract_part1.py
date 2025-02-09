from abstraction import Vehicle

class Bike(Vehicle):
    def __init__(self, n,gear):
        super().__init__(n)
        self.gear = gear

    def show(self):  ##method ko name same hunu parxa abstract method ko jastai ##yeslai remove garyam vanae bike lai ni abstract class vanxa
        print("i am bike")
    
    def show1(self): ##jati oota abstract method xa sabai lekhnu parxa once we inherit Vehicle(abstract class)
        pass

class scooty(Vehicle):
    def __init__(self, n,color):
        super().__init__(n)
        self.wheel = color

    def show(self):
        print("i am scooty")

    def show1(self):
        pass

class truck: #if we donot inherit vehicle(Abstract class) then it is independent normal class so no abstract method needed concrete method is fine
    # def __init__(self, n,tier):
    #     super().__init__(n)
    #     self.tier = tier

    def show(self):
        print("i am truck")

    # def show1(self):
    #     pass