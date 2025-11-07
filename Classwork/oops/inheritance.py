class A:
    def Amethod(self):
        print("A method calling")  

# multilevel inheritance
# class B(A): 
#     def Bmethod(self):
#         print("B method calling")
# class C(B):
#     def Cmethod(self):
#         print("C method calling")
# b=B()
# b.Amethod()
# b.Bmethod()


# multiple inheritnce
# class B: 
#     def Bmethod(self):
#         print("B method calling")
# class C(A,B): 
#     def Cmethod(self):
#         print("C method calling")
# c=C()
# c.Amethod()
# c.Bmethod()
# C.Cmethod()




# Example:

class Animal:
    def setname(self,name):
        self.name=name

class Dog(Animal): 
    def __init__(self, name):
        self.setname(name)

    def disp(self):
        print(self.name)

d = Dog("tommy")
d.disp()