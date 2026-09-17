#write a programm to read to list num and denum which contains the numerator and denominator of a fraction at respective indexs display the smallest fraction along with it index.
num=eval(input("Enter the numerators as a list: "))
denum=eval(input("Enter the denominators as a list: "))
if len(num) != len(denum):
    print("The lengths of the numerator and denominator lists must be the same.")
else:
    small=num[0]/denum[0]
    for i in range(len(num)):
        fr=num[i]/denum[i]
        if fr<small:
            small=fr
            index=i                                                                     
print("The smallest fraction is", small, "at index", index)