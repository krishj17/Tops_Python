class parent1:
    def disp(self):
        print("parent 1 call")

class child1(parent1):
    def c1(self):
        print("child 1 call")
    def disp(self):
        super().disp()
        print("click disp")

c1 = child1()
c1.c1()
c1.disp()