name = "rohan"
print("global name: ", name)

def local():
    name = "krish"
    print("local name: ", name)
local()

print("global name: ", name)