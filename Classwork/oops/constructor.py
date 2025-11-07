# We create constructor in py using __init__ function.
# class student:
#     def __init__(self,name,age): # Parameterised Constructor.
#         self.name = name
#         self.age = age
    
#     def display(self):
#         print(self.name, self.age)

# s1 = student("krish",20)
# s1.display()


# class student:
#     def __init__(self,name,age=18): # Default Constructor.
#         self.name = name 
#         self.age = age
    
#     def display(self):
#         print(self.name, self.age)

# s1 = student("muskeh")
# s1.display()



class student:
    clg = "sdj"

    @classmethod
    def disp(self):
        print("class method:- ", self.clg)

    @staticmethod  # acts like normal function. dont need to decalre self keyword, and thus cannot access data members
    def test():
        print("Static method test called.")


student.disp()
student.test()