class Employee:    
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary

    def display(self):
        print("Employee display")
        print("Empid: ",self.emp_id, "\tName: ",self.name,"\tSalary",self.salary)
