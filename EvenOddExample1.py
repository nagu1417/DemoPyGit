
def countEvenandOdd(list):
    even=0
    odd=0
    for i in list:
        if(i%2==0):
            even=even+1
        else:
            odd=odd+1
    return even,odd


list1=[22,23,45,44,56,23,33,77,90,33,44]
e1,o1=countEvenandOdd(list1)
#print("even value and odd value:",e1,o1)
print("even value:{} and odd value:{}".format(e1,o1))



