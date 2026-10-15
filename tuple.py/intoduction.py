#write a programm to print a fibonacci in a list format..
while True:
 n=int(input("Enter the number of terms: "))
 f=0
 s=1
 l=(f,s)
 for i in range(n-2):
    t=f+s
    l=l+(t,)
    f=s
    s=t
 print(l)