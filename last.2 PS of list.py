#program to find 3rd largest number
n=eval(input("enter the list:"))
l=0
sl=0
tl=0
for i in n:
    if i>l:
        tl=sl
        sl=l
        l=i
    elif i>sl:
        tl=sl
        sl=i
    elif i>tl:
        tl=i
print("third largest num of list is",tl)