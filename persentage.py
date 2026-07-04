while True:
 m=eval(input("enter your maths number"))
 s=eval(input("enter your science number"))
 ss=eval(input("enter your social science number"))
 cs=eval(input("enter your computer science number"))
 e=eval(input("enter your english number"))
 h=eval(input("enter your hindi number"))
 tn=(m+s+ss+cs+e+h)
 print("total number is",tn)
 p=(tn*100)/600
 # i use this 600 because in general there are 6 subjects and each one is of 100
 print("percentage",p)
