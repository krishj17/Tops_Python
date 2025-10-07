# Iterator in Python:--
li = [10,20,30,40,50,60]
# itr = iter(li)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

# Generator in Python:-- (Making our own iterator)

def square(a):
    for i in range(a):
        yield i*i

# itr = iter(square(10))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))