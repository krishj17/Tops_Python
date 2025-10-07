t1 = (100,200,300,400,400)
t2 = ("apple","banana","cherry")
print(t1.index(200))
print(t1.count(400))

t3 = t1 + t2;   print(t3)

t4 = t1*2;   print(t4)

# unpacking:
(a,b,c)=t2;   print(a,b,c)

(a,*b)=t2;   print(a,b)