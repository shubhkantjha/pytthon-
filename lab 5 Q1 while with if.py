num=int(input("enter the number"))
fact=1
while(num!=1):
    if(num==2):
        fact=fact*2

    else:
        fact=fact*num
    num=num-1    

print(fact)        
