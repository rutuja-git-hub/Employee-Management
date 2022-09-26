from Manager import Manager

class SalesMgr(Manager):
    def __init__(self,emp_id,name,salary,incentives,salescount):
        super().__init__(emp_id,name,salary,incentives)
        self.salescount=salescount
    
    def display(self):
        super().display()
        print("SalesCount",self.salescount)

x=SalesMgr('3451','Rutuja Kadam','35000','2500','10')
x.display()
