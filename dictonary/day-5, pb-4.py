#write a programm to create a dictonary which trcks the occurance of characters in a string.
s=input("Enter a string: ")
d={}
for i in s:
    if i not in d:
        d[i]=s.count(i)
       
print(d)







                                                #or
s=input("Enter a string: ")
d={}
for i in s:
    if i in s:
        d[i]=+1
    else:
        d[i]=1
print(d)




                                                                                     
   