class student:

    #intialize gareko variable,intialize matra garna milxa ya
    def __init__(self): 
        self.name = "saraswoti"
        self.age = 22

    #ya nirw print garna aarko banaunu parxa
    def show(self):
        print(self.name,self.age)

a = student()
a.show()  #object through function call garya ani print hunxa vitrw ko
print(a.name) #object bata access garya value variable

