class Employee:
    # Name, Age, Salary
    def __init__(self, name,age , salary):
        self.name = name
        self.age = age
        self.salary = salary


class Company:
    employeeList = []

    def __init__(self,name):
        self.name = name
        self.employeeList = []

    def addEmployee(self,employee):
        self.employeeList.append(employee)
    
    def printEmplyeeCount(self):
        return len(self.employeeList)    
    
# tcs = Company("tcs")
# infosys = Company("infosys")
# emp1 = Employee("Anand","20","10000")
# emp2 = Employee("Venkat","21","2121")
# emp3 = Employee("Arun","21","2121")
# emp4 = Employee("Ajay","21","2121")
# tcs.addEmployee(emp1)
# tcs.addEmployee(emp2)
# infosys.addEmployee(emp3)
# infosys.addEmployee(emp4)
# print(tcs.printEmplyeeCount())
# print(infosys.printEmplyeeCount())


#Dictionary
car={
"Tamilnadu" : [12,24],
"Krishnagiri" : [32,32]
}
#Tuple
colors=('anandha bhavan','saravana bhavan') 
#List
carcompany=['maruthi', 'audi', 'bmw', 'lambogini']
print(carcompany[0])



