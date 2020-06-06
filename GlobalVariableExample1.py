

a=10
b=20

def func1():
    #print("Inside function",a)
    #global a
    x=globals()['a']
    print("a value using x in function",x)
    print("address of x",id(x))
    a=20
    print("Inside function a value",a)
    print("address of a inside function",id(a))
    globals()['a']=20
    print("after changing value")
    print("a value using x in function", x)
    print("address of x", id(x))


func1()
print("outside function a value",a)
print("address of a outside function",id(a))
print("address of b",id(b))