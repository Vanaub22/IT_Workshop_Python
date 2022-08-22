#Write a Python program to add a prefix text to all of the lines in a string.
s=input("Enter the string: ")
lines=[]
lines=s.split(".")
pref=input("Enter the prefix string: ")
for i in range(len(lines)-1):
    print(pref+lines[i].strip())
else:
    print(lines[len(lines)-1])  