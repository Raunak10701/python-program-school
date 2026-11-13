#repetttatrly ask a user to enter the team names   and how many games the team has won and how many they lost store this info in a dictonary where leys are the team names and the values are the list of the form [win,lost]
d={}
ch="yes"
while ch=="yes":
    teamname=input("enter team name: ")
    wins=int(input("enter the no. of matches they won: "))
    loss=int(input("enter the no. of matches they lost: "))
    mdata=[wins,loss]
    d[teamname]=mdata
    ch=input("wants to enter more team data yes/no:")
print (d)

# 1) using the dictonary above allow the user to enter team name and print out teams winning percentage.
n=input("enter the team name :")
winpercentage=(d[n][0]/sum(d[n]))*100
print ("winning percentage of ",n,"is",winpercentage,"%")

#2) using the dictonary create a list whose entries are numbers of wins of each team 
win_list=[d[teamname][0] for teamname in d]
print("List of wins for each team:", win_list)

                #OR

l=[]
for i in d:
    l.append(d[i][0])
print("List of wins for each team:", l)