import itertools
list1=["1","2","3"]
list2=["2","1","3"]
for i,j in zip(list1,list2):
    if i==j :
        print(i,j)
