#write a program to accept the list of numbers from user and raplces the elements at indexes which are multiple of 3 by the cube of the number at that index.eements at the other indexes should remain unchanged for example if user enters the list [3,5,5,2,8,9,7,21,6,5,4]
#output should be [27,5,5,8,8,9,343,21,6,125,4]
l=eval(input("Enter the list of numbers separated by (,) : "))
n=[]
for i in range(len(l)):
    if i%3==0:
        n.append(l[i]**3)
    else:
        n.append(l[i])
print("Modified list:", n)