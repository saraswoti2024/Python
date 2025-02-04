##multiple ma same fucntion name call huda override hunxa ani kun aagadi print hunxa tyo MRO lae resolve garxa
##diamond problem
# '''
# in diamond shape so diamond problem
#           parent
#         /       \
#     child1      child2
#         \       /  
#           child3
# '''
###simple example
# class A:
#     def display(self):
#         print("from A")

# class B(A):
#     def display(self):
#         print("From B")

# class C(A):
#     def display(self):
#         print("from C")

# class D(B,C):
#     def display(self):
#         print("from D")

# d1 = D()
# d1.display()
# print(D.mro())##D,B,C,A,object , pahili aafnai parent class ko left to right tespaxi parent class ko ni parent class

##advance problem
##dont inherite parent class 3,4 oota thau ma ekaichoti ani last ma aajhai sabai lai inherite garne aarko class ma
##duichoti vanda badi dont do it MRO conflict hunxa,inherite garepaxi tesko property ni aauxa ani kna garnu so dont do it will throw error
class A:
    def display(self):
        print("A")
class B:
    def display(self):
        print("B")
class C:
    def display(self):
        print("C")
class D:
    def display(self):
        print("D")
class E:
    def display(self):
        print("E")
class F(B,C,D):
    def display(self):
        print("F")
class G(B,E):
    def display(self):
        print("G")
class H(D,A):
    def display(self):
        print("H")
class Z(F,G,H):
    def display(self):
        print("Z")

z1 = Z()
z1.display()
print(Z.mro())
##calculation of linearization -  zfgbehcdao (calculation c3lineraization folder ma xa)

# print(F.mro())
# print(G.mro())
# print(H.mro())