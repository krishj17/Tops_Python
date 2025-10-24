string="jbsad3332 djbqwdc24 wddqwx24 dd 3412"

# print(len(string))
# print(string.lower())
# print(string.upper())
# print(string.capitalize())
print(string.title())
print(string.strip())
print(string.replace("w","W"))
print(string.find("dd"))
print(string.startswith("j"))
print(string.endswith("2"))
print(string.split(" "))
print(string.join(["hello", "world"]))

print("hello".isalpha())
print("12345".isdigit())
print("hello123".isalnum())



# calc total alphabet and total number in string.
alpha=0; digit=0
for i in string:
    if(i.isalpha()):
        alpha+=1
    elif(i.isdigit()):
        digit+=1
# print(alpha,digit)
