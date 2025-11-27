class animal:
    def disp(self):
        print("its animal")

class dog(animal):
    def name(self):
        print("its a dog")

class puppy(dog):
    def months(self):
        print("its a 6 months puppy")

p = puppy()
p.disp()
p.name()
p.months()