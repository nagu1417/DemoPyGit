def bubbleSort(list1):
    for i in range(0,len(list1)-1):
        for j in range(0,len(list1)-1-i):
            if(list1[j]>list1[j+1]):
                # temp=list1[j];
                # list1[j]=list1[j+1];
                # list1[j+1]=temp;
                list1[j],list1[j+1]=list1[j+1],list1[j];

    print(list1)

list1=[2,8,9,21,4,6,3]
bubbleSort(list1);
