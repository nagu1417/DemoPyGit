nums=[2,6,9,13,17,21,27,30]

for num in nums:
    if(num%11==0):
        print(num)
        break
else:
        #print("Not a multiple of 11",num)
        print("Not found")