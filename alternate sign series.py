x=int(input("enter the value of x:"))
n=int(input("enter the value of n:"))
sum=0
sign=1
for i in range(1,n+1):
    sum=sum +((x**i)/i)*sign
    sign=sign*-1
print("sum of the following series is",sum)