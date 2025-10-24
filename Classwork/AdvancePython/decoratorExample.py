# Only Allow User to See username and Sensitive info if the username contains only alphabet/number, both alpha and num.

def onlyChar(display):
    def wrapper(name):
        if(name.isalpha()==True):
            print("Username Accepted")
            display(name)
        else:
            print("Invalid Username")
    return wrapper

def onlyNum(display):
    def wrapper(name):
        if(name.isdigit()==True):
            print("Username Accepted")
            display(name)
        else:
            print("Invalid Username")
    return wrapper

def bothChNum(display):
    def wrapper(name):
        if(name.isalnum()==True):
            print("Username Accepted")
            display(name)
        else:
            print("Invalid Username")
    return wrapper

# @onlyChar
# @onlyNum
@bothChNum
def display(name):
    print(f"Your name:{name} | Sensitive Info .....")

display("12323#$#")

