#write a programm to read a list of numbers from a user and identify and print all prime numbers in that list.
l=eval(input("enter the numbers of list seperatd by commas and spaces:"))
print("prime numbers list from list l")
for i in l:
    hello=0
    for j in range(2,(i//2)+1):
        if i%j==0:
            hello=1
    if hello==0:
      print(i)


