list1=['abc','xyz','aba','1221']
n=0
count=0
while(n!=len(list1)):
    x=list1[n]
    if x[0]==x[-1]:
        count=count+1
         
    n=n+1  
print(count)      
