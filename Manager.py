from Emp import Employee

class Manager(Employee):
    def __init__(self,emp_id,name,salary,incentives):
        super().__init__(emp_id,name,salary)
        self.incentives=incentives

    def display(self):
        super().display()
        print("Incentives : ",self.incentives)

#x=Manager('3002','Rutuja kadam','34000','2500')
#x.display()
