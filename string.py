#write a programm to input a line of text and input a no of uppercase ,lowecase,digits ,space.
n=input("Enter a line of text: ")
uppercase=0
lowercase=0
digits=0
space=0
for i in n:
    if i.isupper():
        uppercase+=1
    elif i.islower():
        lowercase+=1
    elif i.isdigit():
        digits+=1
    elif i.isspace():
        space+=1
print("Number of uppercase letters:", uppercase)
print("Number of lowercase letters:", lowercase)
print("Number of digits:", digits)
print("Number of spaces:", space)