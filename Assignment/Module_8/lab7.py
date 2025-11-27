no1 = int(input("Enter no1: "))
no2 = int(input("Enter no2: "))
c = input("Enter choice (+,-,*,/): ")
try:
    if(c=='+'):
        print(no1+no2)
    elif(c=='-'):
        print(no1-no2)
    elif(c=='*'):
        print(no1*no2)
    elif(c=='/'):
        print(no1/no2)
    else:
        print("Wrong choice")
except ZeroDivisionError as e:
    print(f"You cannot divide {no1} by {no2}")
except Exception as e:
    print(e)

    