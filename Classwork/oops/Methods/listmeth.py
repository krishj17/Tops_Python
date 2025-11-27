# li=[10,20,30,40,'a',"hello",12.25]

# basics:
# print(li)
# print(li[2])
# print(li[2:5])

# methods:
# li.insert(2,"inserted"); print(li)
# li[2:5] = ["krish","yash","mihir"]; print(li)
# li.append(777); print(li)

a=[10,20,30,40]
# b=['a','b','c','d']
# a.extend(b); print(a)

# a.remove("b"); print(a)
# a.pop(2); print(a)
# a.clear(); print(a)
# del a

# print(a.index(30))
# print(a.count(20))
# sort = [1,4,25,24,13]; sort.sort(); print(sort)
# sort = [1,4,25,24,13]; sort.sort(reverse=True); print(sort)
# reverse = [1,4,25,24,13]; reverse.reverse(); print(reverse)

# Comprision Methods:  its basically a shortform to write 
li=["python","java","php","node","sql"]
newli = [item for item in li if item.startswith("p")]
# print(newli)


# Looping through list.
# for i in a:
#     print(i)

# i=0
# while i<len(a):
#     print(a[i])
#     i+=1