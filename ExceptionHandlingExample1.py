
a=2;
b=10;
c=0;
list1=[1,4,7]

try:
    print("Resource Opened")
    print(a/c);
except ZeroDivisionError as e:
    print("hey we cant divide a number by zero");
try:
    n=int(input("Enter a number"))
    print(n)
except ValueError as e:
    print("Invalid Value");
try:
    print(list1[5]);
except IndexError as e:
    print("Index might be out of Range",e)


finally:
    print("Resource Closed")
