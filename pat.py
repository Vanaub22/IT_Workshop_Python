#to print given pattern
row=int(input('Enter a number:'))
for i in range(row,-1,-1):
    for j in range(1,i+1):
        print(i,end='')
    print('')