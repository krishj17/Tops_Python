class animal:
    def disp(self):
        print("its animal")

class dog(animal):
    def name(self):
        print("its a dog")


d = dog()
d.disp()
d.name()