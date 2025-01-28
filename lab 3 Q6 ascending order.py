num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))
smallest=num1
if(num2<num1 and num2<num3):
    smallest=num1
elif(num3<num1 and num3<num2):
    smallest=num3
else:
    smallest=num3
greatest=num1
if(num2>num1 and num2>num3):
    greatest=num2
elif(num3>num1 and num3>num2):
    greatest=num3
else:
    greatest=num1

middle=num1
if(num2>num3 and num1>num2):
    middle=num2
elif(num3>num1 and num1>num3):
    middle=num3
else:
    middle=num1
print("the ascending order is:",smallest,middle,greatest)    
