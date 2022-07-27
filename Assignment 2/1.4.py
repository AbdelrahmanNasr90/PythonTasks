
class Employee:
    def __init__(self,id,FirstName,LastName,Salary):
        self.id=id
        self.FirstName=FirstName
        self.LastName=LastName
        self.Salary=Salary
    def getid(self):
        return self.id
    def getFirstName(self):
        return self.FirstName
    def getLastName(self):
        return self.LastName
    def getFullName(self):
        return (self.FirstName + " " +self.LastName)
    def getSalary(self):        
        return self.Salary
    def getAnnualSalary(self):        
       return (self.Salary*12)
    def raiseSalary(self, percent):    
     self.Salary+=(self.Salary*(percent/100))    
     return self.Salary
    def Info(self):
        print(f" ID= {self.id} \n FullName= {self.getFullName()} \n Salary= {self.Salary}") 

emp=Employee(19102616,"Abdelrahman","Nasr",1000000)
emp.Info()
print(f"the AnnualSalary is = {emp.getAnnualSalary()}")
print("raiseSalary is ",emp.raiseSalary())