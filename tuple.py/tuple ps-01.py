#given a tuple pairs --------  count the number of pairs which have both digits even.
t=eval(input("enter pairs of tuple:"))
count=0
for i in t:
    if i[0] % 2==0 and i[1]%2==0:
        count+=1
print("numbers of even pairs is ",count)