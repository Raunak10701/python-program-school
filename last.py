#write a programm to input a line of text and count and print numbert of words which contains 2 or moree than 2 vowels in it.
s=input("Enter a line of text: ")
n=0
word=s.split()
for x in word:
    count=0
    for i in range(len(x)):
        if x[i] in "aeiouAEIOU":
            count+=1
    if count>=2:
        n+=1
        print (x)
print("Number of words with 2 or more vowels:", n)
