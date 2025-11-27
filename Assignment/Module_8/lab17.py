class parent1:
    def d2(self):
        print("parent 1 call")

class child1(parent1):
    def c1(self):
        print("child 1 call")

class child2(parent1):
    def c2(self):
        print("child 2 call")

class grandchild(child1, child2):
    def gc(self):
        print("grand child call")

gc = grandchild()
gc.gc()
gc.d2()
gc.c2()
gc.c1()