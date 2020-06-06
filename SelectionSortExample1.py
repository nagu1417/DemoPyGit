
def selectionSort(list2):
    for i in range(len(list2)):
        minpos=i;
        for j in range(i,len(list2)):
            if list2[j]<list2[minpos]:
                minpos=j;
        list2[i],list2[minpos]=list2[minpos],list2[i]

    print(list2)

list2=[8,9,2,11,13,5,4]
selectionSort(list2)