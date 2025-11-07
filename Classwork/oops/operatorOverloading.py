class calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self, obj):
        return calc(self.a + obj.a, self.b + obj.b)

    # def __repr__(self):   # optional, just for pretty printing
    #     return f"calc({self.a}, {self.b})"
c1 = calc(10,20)
c2 = calc(100,200)
c3 = calc(1000,2000)
add = c1+c2
k = add+c3
print(k)