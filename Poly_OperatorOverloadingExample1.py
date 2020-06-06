
# class Example:
#
#     a=6;
#     b=9
#     print(a+b);
#     print("Adding using Method:",a.__add__(b))
# e1=Example();


class Student:
    def __init__(self,m1,m2):
        self.m1=m1;
        self.m2=m2;

    def __add__(self, other):
        sum1=self.m1+other.m1;
        sum2=self.m2+other.m2;
        return sum1+sum2;

    def __gt__(self, other):
        val1=self.m1+self.m2;
        val2=other.m1+other.m2;
        if(val1>val2):
            return True;
        else:
            return False;

s1=Student(22,33);
s2=Student(20,30);
#print(s1+s2)

if s1>s2:
    print("s1 is bigger")
else:
    print("s2 is bigger")

