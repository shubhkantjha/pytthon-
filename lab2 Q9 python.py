n=int(input())
for i in range(1,n+1):
    if(n%n-i==0):
        print("this is not a prime number")
        break
    else:
        print("this is a prime number")
        break
