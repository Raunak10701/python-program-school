#create a dictonary whose leys are months name and whose values are no. of days in corresponding months.
d={}
for i in range(12):
    months=str(input("enter month name : "))
    days=int(input("enter days : "))
    d[months]=days
print(d)



#ask the use to enter the month name and use the dictonery how many days in months.
monthname=input("enter month name to find no of days : ")
d=d[monthname]
print (d)