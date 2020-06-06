pos=-1
def search(list,valueToSearch):
    for i in list:
        if(i==valueToSearch):
            globals()['pos']=i+1;
            return  True,pos;

    else:
        return  False;



list1=[3,5,4,9,6,11,44,22,8]
n=22;

if search(list1,n):
    print("Found at",pos);
else:
    print("Not Found")