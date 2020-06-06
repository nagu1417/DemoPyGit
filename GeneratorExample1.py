

def squareOfValue():
    n = 1
    while n<=10:
            val=n*n;
            yield val
            n+=1;

values=squareOfValue();
print(values)
print(values.__next__())
for i in values:
    print(i);