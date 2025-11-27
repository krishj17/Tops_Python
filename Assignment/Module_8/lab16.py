class parent1:
    def d2(self):
        print("parent 1 call")

class child1(parent1):
    def c1(self):
        print("child 1 call")

class child2(parent1):
    def c2(self):
        print("child 2 call")

c1 = child1()
c1.c1()
c1.d2()

c2 = child2()
c2.c2()
c2.d2()