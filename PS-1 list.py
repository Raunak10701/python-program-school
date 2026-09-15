#write a programm in python to find maximum and minimum number in a list.
n=eval(input("Enter the number of elements in the list: "))
maxnum=0
minnum=n[0]
for i in n:
    if maxnum<i:
        maxnum=i
    if minnum>i:
        minnum=i
print("The maximum number in the list is: ", maxnum)
print("The minimum number in the list is: ", minnum)
