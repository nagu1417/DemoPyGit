
class  Employee:

    companyName="Oracle"

    def __init__(self,name,id):
        self.name=name
        self.id=id

    def get_Name(self):
        return self.name;
    def get_Id(self):
        return self.id

    def set_Name(self,newName):
        self.name=newName;

    def set_id(self,newId):
        self.id=newId;

    @classmethod
    def getCompanyName(cls):
        return Employee.companyName

    @staticmethod
    def info():
        print("100 Employees are working in Oracle")

e1=Employee("abc",111)
e2=Employee("xyz",222)
print(e1.name,e1.id)
print(e2.name,e2.id)
print(Employee.getCompanyName())
print(Employee.info())
