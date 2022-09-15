#Write a Python program to copy the contents of a file to another file
f1=open("test.txt","r")
f2=open("copy.txt","w")
for i in f1.readlines():
    f2.write(i)
f1.close()
f2.close()
print('The contents of the copied file copy.txt is as follows:')
f2=open("copy.txt","r")
print(f2.read())
f2.close()