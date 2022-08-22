#to count the even and odd numbers in a list
list=[]
num=even=0
n=int(input('Enter the number of items in the list:'))
for i in range(n):
    print('Enter the item',i+1,':',end=' ')
    list.append(input())
print('User-input list is as follows:',list)
for i in range(n):
    if(list[i].isdigit()):
        num+=1
        if(int(list[i])%2==0):
            even+=1
print('Number of Even numbers in the list=',even)
print('Number of Odd numbers in the list',num-even)