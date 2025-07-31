class Animal:       #Parent class
    def __init__(self,name):
        self.name = name
        print(f"Animal Created:{self.name}")
    
class Dog(Animal):      #child class
    def __init__(self,name,breed):
        Animal.__init__(self,name)  #Direct call to parent class constructor
        self.breed = breed
        print(f"Dog created: {self.name}, Breed: {self.breed}")

#example
d = Dog("Max","Golden Retriever")




