class salary:
    def __init__(self,amt,bonus):
        self.amt = amt
        self.bonus = bonus

    def dispSalary(self):
        print(self.amt, self.bonus)

class emp:
    def __init__(self,id,name,sal):
        self.id = id
        self.name = name 
        self.sal = sal  # Store the salary object as an attribute

    def dispEmp(self):
        print(self.id, self.name)
        self.sal.dispSalary()  # Display salary details too

sal = salary(10000, 2000)
e = emp(101,"krish",sal)
e.dispEmp()