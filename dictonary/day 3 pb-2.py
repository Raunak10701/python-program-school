#create a dictonary whose leys are months name and whose values are no. of days in corresponding months.
d={"january":31, "february":28, "march":31, "april":30, "may":31, "june":30, "july":31, "august":31, "september":30, "october":31, "november":30, "december":31}




#ask the use to enter the month name and use the dictonery how many days in months.
monthname=input("enter month name to find no of days : ")
m=d[monthname]
print (m)



#print all the keys in alphabetical order.
print(sorted(d))