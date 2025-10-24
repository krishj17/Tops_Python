#  Simple Exception Structure:--
# print("---------------Start")
# try: 
#     # print("krish"+17)
#     print(int("abc"))

# except Exception as e:  # Executes if error occures.
#     print("Exception : ",e)

# else:   # Executes only if no error occures.
#     print("No Error!")

# finally:    # Executes anyway even if error is found or not.
#     print("Program Ended")

# print("---------------End")


# Different Type of Exceptions being handeled here:------------
print("---------------Start")
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


# Actual use of finally, here if you remove finally print function will not get called.
def test():
    try:
        print("hello"+123)
        return 10
    except Exception as e:
        print(e)
        return 0
    finally:
        print("function ended")

test()