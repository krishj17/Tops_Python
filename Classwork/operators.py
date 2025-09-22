# assignment operator
# a=10; c=a
# print(c)
# c+=a
# print(c)
# c-=a
# print(c)
# c*=a
# print(c)
# c/=a
# print(c)

# c=10; x=2
# c**=x
# print(c)
# c//=a
# print(c)

# comparison operator

# print(10<20)
# print(10>20)
# print(10>=20)
# print(10<=20)
# print(10==20)
# print(10!=20)


# identity operator
# In python when we declare a and then we declare b with the same value then python does not create
#   another object to store the value instead it reffrs the value of a. same as pointer does.
#   however this it not the case with list, tuple, etc.
a="hello"
b="hello"
print(a is b) #returns true 

a=[10,20]
b=[10,20]
print(a is b) # returns false even though both are same.


# membership operator

a = [10,20,30,40]
print(10 in a) # true
print(100 not in a) # true