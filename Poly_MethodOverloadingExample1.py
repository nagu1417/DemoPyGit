class Example1:


    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c;
        elif a!=None and b!=None:
            s=a+b;
        else:
            s=a;

        return s


e1=Example1();
result=e1.add(5,8)
print(result)
