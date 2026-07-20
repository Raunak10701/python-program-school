n=eval(input("enter numbers"))
for i in range (2,n+1):
    fact =1
    for j in range(2,i+1):
        fact=fact*j
    print("factorial of",i,"is",fact)
