def hello():
    print("Hello World 123")
# hello()

def mul(a,b):
    print(a*b)
# mul(10,20)

def add(a,b):
    return a+b
# print(add(10,20))


# Default and Keyword Arguments:-----
def person(id=111,name="unknown",age="18+"): # default argument.
    print(id,name,age)
# person("rahul",23)  # default argument problem -> it gives rahul to id and 23 to name if first argument is not provided .

def child(id=101,name="unknown",age="18+"): #keyword argument.
    print(id,name,age)
# child(name="rahul",age=12)  


# Arbitary Arguments:-----
def add(*item): # It can take multiple arguments as parameters and convert them into tuple under one arbitary argument.
    sum=0
    for i in item:
        sum=sum+i
    print(sum)
# add(10,20,30,40)
def add(**item): # It can take multiple arguments as parameters and convert them into dictionary under one arbitary argument.
    print(item)
# add(name="rohit", age=23)


# Lambda Function:-----
sq = lambda a: a*a
area = lambda a,b: a*b
# print(sq(10), area(10,20))


# Concept of Global Keyword:-----
# by default a will remain 10 if we dont use (global a) inside the function. we use (global a) to change the global value of a.
a=10
def change():
    global a
    a=20
    print(a)
# print("before: ",a)
# change()
# print("after: ",a)


# Recursion:-----
def recurs(a):
    print(a)
    a+=1
    if(a<10):
        recurs(a)
# recurs(1)


# Map, Filter, Reduce:-----   (applys a specific function to each list members.)
# Map in Python:-- (apply a function to every item in an array and create a new object containing the transformed results.)
l = [1,2,3,4,5]
sq = map(lambda i:i*i, l)
# print(list(sq))

# Filter in Python:--  (create a new array that contains only the elements from the original array that satisfy a specific condition.)
l = [12,32,43,1,34,53,45,23]
odd = filter(lambda i:i%2!=0, l)
# print(list(odd))

# Reduce in Python:--
from functools import reduce
l = [12,32,43,1,34,53,45,23]
min = reduce(lambda x,y: x if x<y else y, l)
max = reduce(lambda x,y: x if x>y else y, l)
sum = reduce(lambda x,y: x+y, l)
# print(min, max, sum)



# Practice
arr = ["python", "java", "android", "html", "css"]
a = filter(lambda i:"a" in i, arr)  # return items that contain a.
l = map(lambda b: len(b), list(a))
# print(list(a), list(l))

