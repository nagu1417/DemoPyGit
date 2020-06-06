class A:

    def f1(self):
        print("In F1 method");

    def f2(self):
        print("In F2 method");

class B(A):
    def f3(self):
        print("In F3 method");

    def f4(self):
        print("In F4 method");

a1=A();
b1=B();
# a1.f1();
# a1.f2()
b1.f3();
b1.f4();
b1.f1()
b1.f2()
