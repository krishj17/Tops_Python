class Animal:
    def speak(self):
        """Generic sound that all animals can make."""
        return "The animal makes a sound."
class Dog(Animal):
    def speak(self):
        print("woof woof")

class Cat(Animal):
    def speak(self):
        print("meow meow")

a = Animal()
d = Dog()
c = Cat()

d.speak()
c.speak()
