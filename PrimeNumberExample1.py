num= int(input("Enter a number:"))
for i in range(2,num):
    if(num%i==0):
        print("Not a prime num9ber")
        break
else:
    print("Given number is prime")
