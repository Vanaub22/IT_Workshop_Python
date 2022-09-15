#Write a Python program to read first n lines of a file
f=open("test.txt")
for i in range(1,int(input('Enter the number of lines to read(n): '))+1):
    print(f.readline())
f.close()