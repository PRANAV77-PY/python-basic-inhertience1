#vehicle example

class Vehicle:          #Parent class
    def __init__(self,model):
        self.model = model
        print(f"Vehicle Created:{self.model}")


class Bike(Vehicle):    #child class1
    def __init__(self,model,speed):
        Vehicle.__init__(self,model)
        self.speed = speed
        print(f"Bike Created:{self.model},Speed:{self.speed}")



class Car(Vehicle):     #child class2
    def __init__(self,model,speed):  
        Vehicle.__init__(self,model)
        self.speed = speed
        print(f"Car Created:{self.model},Speed:{self.speed}")


#object Creation
b = Bike("Activa",50)
c = Car('Tesla',40)