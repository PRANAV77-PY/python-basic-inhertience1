#Define a Bank Class
class Bank:
    def __init__(self,name):
        self.name = name
        print(f"Bank Created Account:{self.name}")

class Balance(Bank):
    def __init__(self,name,amount):
        Bank.__init__(self,name)
        self.amount = amount
        print(f"Balance Created Account:{self.name},Amount Created: {self.amount}")

class Loan(Bank):
    def __init__(self,name,amount):
        Bank.__init__(self,name)
        self.amount = amount
        print(f"Loan Created Account:{self.name},Loan Created:{self.amount}")

#object creation
b = Balance('vaibhav',20000)
l = Loan('vivek',80000)

