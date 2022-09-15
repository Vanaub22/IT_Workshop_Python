#to print the number of occurrence of the pattern string found in the file
f=open("test.txt","r")
freq=0
pattern_str=input('Enter the pattern string:')
for i in f.readlines():
    if pattern_str in i:
        freq+=1
f.close()
print('The pattern string is:',pattern_str)
print('The pattern string occurs {} times in the file test.txt'.format(freq))