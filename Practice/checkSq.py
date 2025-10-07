import math
li = [2,4,16,12,31,34,21,43,12,32,84]


a = filter(lambda k: math.sqrt(k).is_integer() ,li)
print(list(a))

