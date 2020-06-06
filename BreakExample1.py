
availableChoclates=5
x=int(input("Enter number of Choclates"))
print(x)
i=1
while(i<=x):
    if(i>availableChoclates):
        print("Out of Stock")
        break
    print("Choco")
    i+=1;
print("End");
