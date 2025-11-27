from multipledispatch import dispatch

class areas:
    @dispatch(int)
    def area(self, rad):
        print("calc area of circle")
    
    @dispatch(int,int)
    def area(self, len, bre):
        print("calc area of rect")

a = areas()
a.area(12)
a.area(1,2)