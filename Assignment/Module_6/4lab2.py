n=17

for i in range(2,n):
    if(n%i==0):
        print("not prime")
        break
    if(i+1==n):
        print("prime")