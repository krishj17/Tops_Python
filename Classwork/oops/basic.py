class Pen:
    name="cello px1"
    price=150
    color="Red"
    def to_write(self):
        print("Pen-----------")
        print(self.name, self.price, self.color)


p1 = Pen(); p1.to_write()

p2 = Pen()
p2.price=90
p2.to_write()







class student:
    name="krish"
    age=19
    def display(x):
        print(x.name, x.age)

s1 = student()
s1.display()