from numpy import *;

arr1=array([

    [1,2,3],[2,4,6],[3,6,9],[4,8,12]
])
print(arr1)
print(arr1.dtype)
print(ndim(arr1))
print(arr1.size)
print(arr1.flatten())
print(arr1.reshape(2,2,3))

arr3=array([[1,2,3],[2,1,3]])
arr4=array([[1,3,5],[2,4,6]])
arr5=array([[1,2],[2,3],[3,4]])

m1=matrix(arr3)
m2=matrix(arr4)
m3=matrix(arr5)
print(m1)
print(m2)
m5=m1+m2
print(m5)

m4=m1*m3
print(m4)


m6=transpose(m1)
print(m6)

# arr2=array(
#     [
#         [
#         [1,2,3],[4,5,6]
#         ],
#         [
#          [6,5,4],[3,2,1]
#         ]
#     ]
# )
# print(arr2)
# print(ndim(arr2))