#write a  program tahat the input aline of text and print each word in a seperate line.
# Program to print each word in a separate line
a=input("Enter a line of text: ")
words = a.split()  # Split the string into words
for i in words:
    print(i)  # Print each word on a separate line.