list1=[1,2,3,4]
greatest=list1[0]
for i in range(1,len(list1)):
    if greatest<list1[i]:
       greatest=list1[i]
print(greatest)       
