# Define a fruit class
class Fruits:           #parent class
    def __init__(self,name):
        self.name = name
        print(f"Fruits colour:{self.name}")

class Mango(Fruits):            #child class 1
    def __init__(self,name,price):
        Fruits.__init__(self,name)
        self.price = price
        print(f"Mango:{self.name},Price$:{self.price}")

class Apple(Fruits):           #child class 2
    def __init__(self,name,price):
        Fruits.__init__(self,name)
        self.price = price
        print(f"Apple:{self.name},Price$:{self.price}")

#object Creation
m = Mango('Yellow',30)
a = Apple('Red',50)

        
        
        