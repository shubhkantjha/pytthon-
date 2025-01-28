num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))
if(num1==num2):
    print("first and second numbers are equal:",num1)
elif(num1==num3):
    print("first and third numbers are equal:",num1)
elif(num2==num3):
    print("third and second numbers are equal:",num2)
else:
    print("no one is equal..")
