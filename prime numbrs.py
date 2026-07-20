#write a programmm to print all prime numbers between 2 to 100
n=eval(input("enter number "))
b=eval(input("enter 2nd number "))
for i in range (n,b+1):
    hello=0
    for j in range(2,(i//2)+1):
        if i%j==0:
            hello=1
    if hello==0:
        print(i)
  
