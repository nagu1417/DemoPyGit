
class Company:



    def __init__(self,employeeName,empId):
        print("In Init method")
        self.employeeName=employeeName;
        self.empId=empId;
        #print("employeeName",employeeName,"empId",empId)

    def employee(self):
        print("Employee Name:",self.employeeName," Employee id:",self.empId)


c1=Company("Nagesh",101);
c2=Company("Eswar",102)
c1.employee();
c2.employee()

