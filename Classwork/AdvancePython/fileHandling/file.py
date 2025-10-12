# Write data into text file.
# f = open("D:/KRISH/Tops/Tops_Python/Classwork/AdvancePython/fileHandling/text1.txt","w")
# # f.write("hello 123")
# f.writelines(["hello","\nworld"])
# f.close()

# Append data into text file
# f = open("D:/KRISH/Tops/Tops_Python/Classwork/AdvancePython/fileHandling/text1.txt","a")
# f.write("alpha")
# f.close()

# Read data from file.
# f = open("D:/KRISH/Tops/Tops_Python/Classwork/AdvancePython/fileHandling/text1.txt","r")
# data = f.read()
# print(data)
# data = f.readlines()
# print(data)

# Start with H and lenght of each.
# f = open("D:/KRISH/Tops/Tops_Python/Classwork/AdvancePython/fileHandling/text1.txt","r")
# data = f.readlines()
# l = map(lambda x: len(x), data)
# print(list(l))
# H = filter(lambda x: x.startswith("h") ,data)
# print(list(H))  
# f.close()

# using with we dont need to close the file.
# with open("D:/KRISH/Tops/Tops_Python/Classwork/AdvancePython/fileHandling/text1.txt") as f:
#     data = f.read()
#     print(data)

# with open("D:/KRISH/Tops/Tops_Python/Classwork/AdvancePython/fileHandling/text1.txt") as f:
#     position = f.tell()
#     print(position)
