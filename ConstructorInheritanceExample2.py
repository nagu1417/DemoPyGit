class A:

    def __init__(self):
        print("In Init method of A")
    def f1(self):
        print("In F1 method in A");

    def f2(self):
        print("In F2 method");

class B:
    def __init__(self):
        super(B, self).__init__();
        print("In Init method of B")
    def f1(self):
        print("In F1 method in B");

    def f4(self):
        print("In F4 method");

class C(A,B):
    def __init__(self):
        super().__init__();
        print("In Init Method in C")

c1=C();
c1.f1()