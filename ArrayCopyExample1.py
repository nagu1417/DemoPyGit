from numpy import *

arr1=array([2,15,7,22,9,11,4])
arr2=array([4,22,16,32,2,7])
print(arr1)
print(arr2)

#print(concatenate([arr1,arr2]))
# arr3=arr1;
# print(arr3)
# print(id(arr1))
# print(id(arr3))

#shallow Copy
arr4=arr1.view();
print("Before changing a value")
print(arr1)
print(arr4)
arr1[1]=9
print("after changing a value")
print(arr1)
print(arr4)
print(id(arr1))
print(id(arr4))

#Deep Copy
# arr5=arr1.copy();
# print("Before changing a value")
# print(arr1)
# print(arr5)
# arr1[1]=9
# print("after changing a value")
# print(arr1)
# print(arr5)
# print(id(arr1))
# print(id(arr5))


# print(sin(arr1))
# print(cos(arr2))
# print(len(arr2))
# print(average(arr1))
# print(sqrt(arr2))
# print(sum(arr1))

#Add 4 to each element
# for i in range(len(arr1)):
#      arr1[i]=arr1[i]+4
#
# print("array values after adding 4")
# print(arr1)

#Adding 5 to each element
# print("arr2 values after adding 5")
# arr2=arr2+5
# print(arr2)

