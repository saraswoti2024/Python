##combination of two or more inheritance

class A:
    def display(self):
        print("display from class A")

class B:
    def display(self):
        print("display from class B")

class C(A,B):
    def display(self):
       print("display from class c")

class D(C): #D(A,C)->yo garda error aauxa kina vane c lae tw already inherite garisakyo A,B bata ani feri A garda circular type ko hunxa so error falxa
    def display(self):
        super().display()  ##jaile vitrw hunxa super
        # C().display()
        print("display from class D")

D1 = D()
D1.display()
