cont="t"
print("-------------------")
no1=int(input("->"))
prevamt=no1
while cont=="t":
    choice=input("->")
    no2=int(input("->"))
    if choice=="+":
        result=prevamt+no2
        print("=",result)
    elif choice=="-":
        result=prevamt-no2
        print("=",result)
    elif choice=="*":
        result=prevamt*no2
        print("=",result)
    elif choice=="/":
        result=prevamt/no2
        print("=",result)
    else:
        print("Invalid Operator")
    prevamt=result
    # print("previous amt: ",prevamt)
    cont = input("Continue? (t/f):- ")
