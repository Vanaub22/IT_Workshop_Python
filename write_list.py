#Write a Python program to write a list to a file
f=open("test.txt","w")
lst=input('Enter the items of the list separated by spaces:').split()
for i in lst:
    f.write(i+"\n")
f.close()
print('The contents of the file test.txt are now as follows:')
f=open("test.txt","r")
print(f.read())
f.close()