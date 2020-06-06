
def fact(n):
    value=1
    if n==1:
        return 1
    else:
        value= n*fact(n-1)
    return value


result=fact(5)
print(result)
