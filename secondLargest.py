#to find second largest number in a list
numlist=[]
list=[]
n=int(input('Enter the number of items in the list:'))
for i in range(n):
    print('Enter the item',i+1,':',end=' ')
    list.append(input())
print('User-input list is as follows:',list)
for i in range(n):
    if(list[i].isdigit()):
        numlist.append(list[i])
if(len(numlist)<2):
    print('Not enough numbers in the list...TRY AGAIN')
else:
    numlist.sort(reverse=True)
    print('The second largest number in the list is',numlist[1])