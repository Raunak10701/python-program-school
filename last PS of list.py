#write a program to find the second largest number of list.
n=eval(input("enter the numbers in list:"))
largest=0
seclargest=0
for i in n:
    if i>largest:
        seclargest=largest
        largest=i
    elif i > seclargest:
        seclargest=i
print("second largest no. is",seclargest)
    
