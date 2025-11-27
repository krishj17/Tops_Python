# Note: Here in python there is no specific access specifier methods. but we follow this rule:
# _var for protected
# __var for private
#  
class Test:
    a = 10  # public
    _b = 100    # protected
    __c = 1000    # private
    def disp(self):
        print("printing : ",self.a, self._b, self.__c)

t = Test()
t.a = 50
t._b = 500  # this works but we dont do this in real life projects, we treat protected variables like as they are supposed to.
t.__c = 5000 # this doesnt work because unlike the above two, in private python actually changes the name of private variable(__c)
t.disp()

print(dir(t)) # this returns the all the attributes of the object provided.
# here we can see that python changed the name of private variable from '__c' to '_Test__c'.

t._Test__c = 1234 # cheat code to access and change private variables or attributes.
t.disp()