#print out all the months that have 31 days in them.
d={"january":31, "february":28, "march":31, "april":30, "may":31, "june":30, "july":31, "august":31, "september":30, "october":31, "november":30, "december":31}
for i in d:
    if d[i]==31:
        print(i)




#print out key value pairs sorted by number of days in each month,in a dictonary.
for i in sorted(d, key=d.get):
    print(i, d[i])

                                             #OR


d={"january":31, "february":28, "march":31, "april":30, "may":31, "june":30, "july":31, "august":31, "september":30, "october":31, "november":30, "december":31}
l=[]
for i in d:
    l.append([d[i],i])
l.sort()
dnew={}
for i in l:
    dnew[i[1]]=i[0]
print(dnew)