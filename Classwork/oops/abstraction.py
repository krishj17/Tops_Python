from abc import ABC,abstractmethod
# We cant create objects of abstract methods
# and thus we can only access the variables using the abstract methods in child class. 
class base(ABC): # abstract class.
    a = 10
    @abstractmethod
    def disp(self): # abstract method. its always empty.
        pass

class child(base):
    def disp(self): # using the abstract method to access and use methods and variables of abstract class.
        print(self.a)

c = child()
c.disp()


# Example:-------------------------------------------
class Bank(ABC):
    loan = 0
    @abstractmethod
    def takeLoan(self, amt):
        pass
    @abstractmethod
    def payLoan(self, amt):
        pass
    @abstractmethod
    def getLoanDetail(self):
        print("Current Loan Amt: ", self.loan)

class Account(Bank):
    def takeLoan(self, amt):
        self.loan+=amt
    def payLoan(self, amt):
        self.loan-=amt
    def getLoanDetail(self):
        return super().getLoanDetail()
    
a = Account()
a.getLoanDetail()
a.takeLoan(10000)
a.getLoanDetail()
a.payLoan(3000)
a.getLoanDetail()

