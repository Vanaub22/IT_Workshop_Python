#Write a Python program to count the number of lines in a text file
f=open("test.txt","r")
count=0
for i in f:
    count+=1
print('The number of lines in the file =',count)
f.close()