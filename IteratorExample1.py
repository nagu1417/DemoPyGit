list1=[22,12,33,23,5,9]

# for i in list1:
#     print(i)
# it=iter(list1);
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

class User:
    def __init__(self):
        self.num=1;

    def __iter__(self):
        return self
    def __next__(self):

        if(self.num<=10):
            val = self.num;
            #print(val)
            self.num=self.num+1;
            return val;
        else:
            raise StopIteration;

values=User();
for i in values:
       print(i)