# conditional
# looping
# control

cont = "t"
while cont == "t":
    marks =int(input("Enter Marks: "))
    if marks>=91 and marks<=100: print("A")
    elif marks>=71 and marks<=90: print("B")
    elif marks>=51 and marks<=70: print("C")
    elif marks>=35 and marks<=50: print("D")
    elif marks>=0 and marks<=34: print("F")
    else: print("Invalid Marks")

    cont = input("Do You want to continue: t/f :- ")
