class Student:
        def __init__(self,name,rollNo,Address):
            self.name=name;
            self.rollNo=rollNo;
            self.Address=Address
            #self.address=address;



        def display(self):
            print(self.name,self.rollNo)
            self.Student.Address.display(self)

        class Address:
            def __init__(self,location,zipcode):
                self.location=location;
                self.zipcode=zipcode;
            def display(self):
                print(self.location,self.zipcode)

a1=Student.Address("Hyd",12345)
a2=Student.Address("Ap",54321)
s1=Student("Nagesh",1,a1)
s2=Student("Ramesh",11,a2)

print(s1.display())
print(s2.display())