#write a programm to duplicate elements from the list you are not allowed to create a new list within the program.
l=eval(input("Enter a list using square brackets, commas: "))
for i in l:
    while l.count(i)>1:
        l.remove(i)
print("List after removing duplicates:", l)        
