#write a program that receives a fibonacci sries and returns the number telling which term is this .
n=int(input("Enter a number in the Fibonacci series: "))
f=0
s=1
term=0
for i in range(1,100):
    if n==f:
        term=i
        break
    f,s=s,f+s
print(f"The number {n} is the {term}-th term in the Fibonacci series.") 