while True:
 n=int(input("enter  a nmber"))
 onum=n
 count=0
 while n>0:
    n=n//10
    count=count+1
 n=onum
 res=0
 while n>0:
    r=n%10
    res=res + (r**count)
    n=n//10
 if res==onum:
    print(onum,"is an armstrong")
 else:
    print(onum,"is not an aremstrong")
