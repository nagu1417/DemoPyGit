from array import *

#Creating an array
demoarray=array('i',[2,5,8,9,12,-4])
#printing the array values
print(demoarray)
#appending a value to an array
print(demoarray.append(19))

#printing all values in array using for loop
for i in demoarray:
    print(i)

#printing all values in array using for loop and range:
print("Based on j")
for j in range(5):
    print(demoarray[j])

#buffer_info will return two parameters address and size of array
print(demoarray.buffer_info())

#len prints size of array
print(len(demoarray))

#contains checks whether element is present in array
print(demoarray.__contains__(5))

#reverse() reverses the array
demoarray.reverse()
print("After Reverse")
print(demoarray)

#Creating a new Array using existing array
newArray=array(demoarray.typecode,(a for a in demoarray))
print(newArray)