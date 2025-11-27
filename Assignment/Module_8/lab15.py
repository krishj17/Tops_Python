class parent1:
    def d2(self):
        print("parent 1 call")

class parent2:
    def d1(self):
        print("parent 2 call")

class child(parent1,parent2):
    def c(self):
        print("child call")

c = child()
c.d1()
c.d2()
c.c()