# Define a Company class
class Company:              #Parent class
    def __init__(self,department):
        self.department = department
        print(f"Company departments Created: {self.department}")

class HR(Company):          #child class
    def __init__(self,department,Vacancy):
        Company.__init__(self,department)        #Direct call to parent class
        self.Vacancy = Vacancy
        print(f"HR Vacancy Created:{self.department},Vacancy:{self.Vacancy}")

class Sales(Company):
    def __init__(self,department,marketing):
        Company.__init__(self,department)       #Direct call to parent class
        self.marketing =marketing
        print(f"Sales Created:{self.department},Marketing:{self.marketing}")

#object Creation
h = HR('Software',10)
s = Sales('Project','Project bringing')




