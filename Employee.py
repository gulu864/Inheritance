class Object():
    
    def __init__(self,Name,IDnumber):
        self.Name = Name
        self.IDnumber = IDnumber
    def Showcase(self):
        print(self.Name)
        print(self.IDnumber)

class Employee(Object):

    def __init__ (self,Name,IDnumber,salary,post):
        self.salary = salary
        self.post = post
        Object.__init__(self,Name,IDnumber)

var1 = Employee("Rohan", 87553664539 , 986 , "Intern")

var1.Showcase()
print("You are working as", var1.post)