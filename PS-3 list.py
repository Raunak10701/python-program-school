#write  a programm t o read a list from user and  shift all those numbers to another list which are divisible by both 3 and 5.
l=eval(input("Enter the list of numbers separated by (,) : "))
d35 = []
for num in l:
    if num % 3 == 0 and num % 5 == 0:
        d35.append(num)
print("Numbers divisible by both 3 and 5:", d35)