f3=open("TestFile4",'w');
f=open("TestFile",'r')
for i in f:
    print(i)
    f3.write(i);
#print(f.readline(7))

# f1=open("TestFile2",'w');
# f1.write("I am writing something to a new file")
#
# f2=open("TestFile3",'w');
# f2.write(f.read())

# f3=open("TestFile4",'w');
# for i in f:
#     print(i)
#     f3.write(i)