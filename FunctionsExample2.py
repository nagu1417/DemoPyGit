

def update(x):
    print("id of x before update:", id(x))
    x=8
    print("id of x after update:", id(x))
    print("x",x)


# a=10
# print("id of a:",id(a))
# update(a)
# print("a",a)


def updatelist(list1):
    print("id of list1 before update:", id(list1))
    list1[1]=23
    print("id of list1 after update:", id(list1))
    print("list1",list1)


list2=[10,20,30,40]
print("id of list2:",id(list2))
updatelist(list2)
print("list2",list2)