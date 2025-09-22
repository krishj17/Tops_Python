def count(limit):
    for i in range(1, limit + 1):
        yield i

counter = count(3)

print(next(counter)) 
print(next(counter)) 
print(next(counter)) 