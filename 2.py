#write a programm in python which take align of text as input and create a new string by repacing every alpha betic character at even index that is 0,2,4 with the corresponding uppercase character  if the string is welcome allthe output will be ""  
n=input("Enter a line of text: ")
s=''
for i in range(0,len(n)):
    if i%2==0:
        s=s+n[i].upper()
    else:
        s=s+n[i]
print(s)
    