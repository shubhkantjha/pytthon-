list1=[1,2,3,4]
smallest=list1[0]
for i in range(1,len(list1)):
    if smallest>list1[i]:
       smallest=list1[i]
print(smallest)       
