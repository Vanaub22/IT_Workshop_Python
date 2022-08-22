#to interchange the first and last items in a list
list=[]
n=int(input('Enter the number of items in the list:'))
for i in range(n):
    print('Enter the item',i+1,':',end=' ')
    list.append(input())
print('User-input list is as follows:',list)
temp=list[0]
list[0]=list[-1]
list[-1]=temp
print('List after interchanging the first and last items:',list)