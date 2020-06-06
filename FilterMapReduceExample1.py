
from functools import reduce;
def is_even(n):
    return n%2==0

def doubletheNum(n):
    return n*2;

def add_all(a,b):
    return a+b

list1=[1,3,6,9,4,8,22,44,12,5,17,24,33]

# evenNumbers=list(filter(is_even,list1))
evenNumbers=list(filter(lambda  a: a%2==0,list1))
print("even number",evenNumbers)

#doubles=list(map(doubletheNum,evenNumbers))
doubles=list(map(lambda  n: n*2,evenNumbers))
print("doubles",doubles)

#sum=reduce(add_all,doubles)
sum=reduce(lambda a,b: a+b,doubles)
print("sum",sum)

