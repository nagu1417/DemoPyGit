

def person(name,*data):
    print("Hello")
    print(name)
    print(data)

person('Nagesh',28,'Hyd','8106125')

def person2(name,**data2):
    print(name)
    print(data2)
    for key,value in data2.items():
        print(key,value)

person2(name='Mahesh',age=27,city='Hyd',mob=12345)

