#write a programm to create a tuple and find sum of its alternate elements.
t=eval(input("enter the tuple elements seperated by comma:"))
sum_alternate = 0
for i in range (0,len(t),2):
    sum_alternate += t[i]
print("sum of alternate elements of tuple is:",sum_alternate)
    