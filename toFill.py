#to fill the text file using trial lines
f=open("test.txt","w")
for i in range(1,21):
    f.write("This is line {}".format(i)+"\n")
f.close()