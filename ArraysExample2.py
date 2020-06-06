from array import *

tempArray=array('i',[])
arraySize=int(input("Enter the size of the array"))

for i in range(arraySize):
        x=int(input("Enter the array value"))
        tempArray.append(x)

print(tempArray)

numtoSearch=int(input("Enter the number to search in array"))
for j in tempArray:
        if(j==numtoSearch):
                print(j)
                print("Number found at index:"+str(tempArray.index(numtoSearch)))
                break

else:
        print(numtoSearch+" Not found")


