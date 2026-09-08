#write a program input line of text all print in reverse order
a=input("Enter a line of text: ")
res=(a.split()[::-1])
for i in res:
    print(i)  # Print each word in reverse order on a separate line.

print(res)