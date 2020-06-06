class Employee:

    def __init__(self):
        self.name="Nagesh"
        self.age=27

    def compare(self,other):
        if(self.age==other.age):
            print("They are  equal")
            return True;
        else:
            print("They are not equal")
            return False;

e1=Employee();
e2=Employee();
e1.age=22
e2.age=24
e1.name="Siva"
e2.name="Mahesh"


print(e1.name,e1.age)
print(e2.name,e2.age)
print(e1.compare(e2))