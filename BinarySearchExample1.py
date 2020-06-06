pos=-1
def binarySearch(list2,valueToSearch):
    lower=0;
    upper=len(list2);
    while lower<=upper:
        mid=int((lower+upper)/2);
        print("Now mid position is:",mid)
        if(valueToSearch>list2[mid]):
            print(valueToSearch," is greater than ",list2[mid]," so making lower position as ",mid)
            lower=mid+1;
        elif(valueToSearch<list2[mid]):
            print(valueToSearch, " is less than ", list2[mid], " so making upper position as ", mid)
            upper=mid-1;
        else:
            print("Value Found at",mid);
            globals()['pos']=mid
            return pos

    else:
        print("Value Not Found")




list2=[4,7,9,11,13,16,18,21,25,33,44,46,57,62,66];
n=10;

if binarySearch(list2,n):
    print("Found at",pos);
else:
    print("Not Found")