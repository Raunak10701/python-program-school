#write a program to create a dictionary which tracks and stores the occurrence of all vowels from a string into a dictonary.
s=input("Enter a string: ")
vowels="aeiouAEIOU"
d={}
for i in s:
    if i in vowels:
        if i not in d:
            d[i]=s.count(i)
print(d)


                                        #OR
S=input("Enter a string: ")
d={}
for i in S:
    if i in "aeiouAEIOU":
        if i in d:
            d[i]=S.count(i)
        else:
            d[i]=1
print(d)
