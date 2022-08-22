#to count the positive and negative numbers in a list
list=[]
pos=neg=0
n=int(input('Enter the number of entries in the list:'))
for i in range(n):
    print('Enter the number',i+1,':',end=' ')
    list.append(input())
print('User-input list is as follows:',list)
for i in range(n):
        if(list[i]>'0'):
            pos+=1
        elif(list[i]<'0'):
            neg+=1
print('Number of Positive numbers in the list =',pos)
print('Number of Negative numbers in the list =',neg)