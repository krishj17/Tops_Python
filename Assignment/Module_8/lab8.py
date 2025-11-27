try:
    print("abc"+123)
    # print(10/0)
    # int("abc")
    # data=[10,20,30]; print(data[5])
    # dict={"name":"krish"}; print(dict["age"])
    # print(abc)
except TypeError as e:   
    print("TypeError : ",e)
except ZeroDivisionError as e:   
    print("ZeroDivisionError : ",e)
except  ValueError as e:   
    print(" ValueError : ",e)
except IndexError as e:   
    print("IndexError : ",e)
except KeyError as e:   
    print("KeyError : ",e)
except NameError as e:   
    print("NameError : ",e)
print("---------------End")