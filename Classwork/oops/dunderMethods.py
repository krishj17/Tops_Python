class test:
    def __init__(self, a, b): 
        self.a = a
        self.b = b
    
    def __add__(self):
        return self.a + self.b

    def __str__(self): # returns below string when printing just class object.
        return "hello"
    
    def __eq__(self, value):    # check if the two objects have equal values.
        return self.a==value.a and self.b==value.b

t1 = test(10,20)
t2 = test(10,20)
print(t1.a + t1.b)  # __add__
# print(t1)     # __str__
# print(t1==t2)     # __eq__


class sample:
    def __init__(self,l):
        self.list = l

    def __len__(self):
        return len(self.list)

    def __setitem__(self,index,value):
        self.list[index] = value
    
    def __getitem__(self,index):
        return self.list[index]


s1 = sample([10,20,30,40,50,60])
print(len(s1))  # __len__
s1[3]=400   # __setitem__
print(s1.list)
print(s1[2])    # __getitem__