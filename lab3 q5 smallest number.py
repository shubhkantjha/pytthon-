num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))
smallest=num1
if(num2<num1 and num2<num3):
    print("second number is samllest:",num2)
elif(num3<num1 and num3<num2):
    print("third number is samllest:",num3)
else:
    print("first number is samllest:",num1)
