#to reverse a list
list=[]
n=int(input('Enter the number of items in the list:'))
for i in range(n):
    print('Enter the item',i+1,':',end=' ')
    list.append(input())
print('User-input list is as follows:',list)
list.reverse()
print('The list in reversed order is as follows:',list)