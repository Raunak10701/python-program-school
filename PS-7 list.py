##write a programm to print the elements of a list that contains atleast one vowel in it.
l=eval(input("Enter a list using square brackets, commas: "))
for i in l:
    for j in i:
        if j in 'aeiouAEIOU':
            print(i)
            break