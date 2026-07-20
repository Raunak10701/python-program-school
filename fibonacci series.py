#write first 10 numbers of fibonacci series
n=eval (input("enter  a number"))
f=0
s=1
print(f,s,end=" ")
for i in range (0,n-2):
    t=f+s
    print(t,end=" ")
    f=s
    s=t
    
    
