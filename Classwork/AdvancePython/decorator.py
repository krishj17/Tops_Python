
# Simple Decorator. 
# Remove @deco and you can call the funtion normally.
# Use @deco to execute a piece of code before the actual function test is called.
def deco(test):
    def wrapper():
        print("Decorator used!")
        test()
    return wrapper

@deco
def test():
    print("hello world")
test()



# Calc:------------------
def add(calc):
    def wrapper(*a):
        print(a[0]+a[1])
        calc(*a)
    return wrapper
def sub(calc):
    def wrapper(*a):
        print(a[0]-a[1]) #10-20 = -10
        calc(*a)
    return wrapper
def mul(calc):
    def wrapper(*a):
        print(a[0]*a[1]) #10-20 = -10
        calc(*a)
    return wrapper

@add
@sub
@mul
def calc(a,b):
    print("Calc Called")
# calc(10,20)
