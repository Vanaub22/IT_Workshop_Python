#To create a list of tuples from given list having number and its cube in each tuple. (e.g. (2,8),(3,27),....)
lst1=[]
i=0
while(True):
	i+=1
	print('Enter the item',i,'or press Enter to Exit:',end=' ')
	x=input()
	if(x!=''):
		lst1.append(x)
	else:
		print('List terminated')
		break
print('User-input list is as follows:',lst1)
lst2=[]#new list to store tuples in the form of (item,cube of item)
for i in range(len(lst1)):
    lst2.append((int(lst1[i]),int(lst1[i])**3))
print('New list of tuples is as follows:',lst2)