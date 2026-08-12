#WRITE A  program to check a pallendeome number
from pickle import TRUE


while TRUE:
 n=int (input("enter a number: "))
 x=n
 count=0
 while n>0:
    n=n//10
    count+=1
 n=x
 p=0
 while n>0:
   r=n%10
   count-=1
   p=p+(r*(10**count))
   n=n//10
 if p==x:
    print("the number is a palindrome") 
 else :
    print("the number is not a palindrome")
   
   
