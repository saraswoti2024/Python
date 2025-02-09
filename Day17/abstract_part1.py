from abstraction import Vehicle

class Bike(Vehicle):
    def __init__(self, n,gear):
        super().__init__(n)
        self.gear = gear

    def show(self):  ##method ko name same hunu parxa abstract method ko jastai ##yeslai remove garyam vanae bike lai ni abstract class vanxa
        print("i am bike")

class scooty(Vehicle):
    def __init__(self, n,color):
        super().__init__(n)
        self.wheel = color

    def show(self):
        print("i am scooty")

class truck(Vehicle):
    def __init__(self, n,tier):
        super().__init__(n)
        self.tier = tier

    def show(self):
        print("i am truck")