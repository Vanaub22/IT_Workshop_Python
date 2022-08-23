# To take a list as input, store the values in the odd index positions in one list and the rest in another
# Finally add the corresponding elements in the two lists
list=[]
lst1=[]
lst2=[]
result=[]
extra=[]
while(True):
	n=int(input('Enter the number of items in the list:'))
	if(n<9):
		print('Minimum number of items should be 9...Try Again')
	else:
		break
for i in range(n):
	print('Enter the item at position',i+1,':',end='')
	list.append(input())
print('The user-input list is as follows:',list)
for i in range(n):
	if(i%2==0):
		lst1.append(list[i])
	else:
		lst2.append(list[i])
print('The list containing items in the odd positions are as follows:',lst1)
print('The list containing items in the even positions are as follows:',lst2)
if(len(lst1)>len(lst2)):
	N=len(lst2)
	extra=lst1[N-1:]	
elif(len(lst1)<len(lst2)):
	N=len(lst1)
	extra=lst2[N:]
for i in range(N):
	if(lst1[i].isalpha() or lst2[i].isalpha()):
		result.append(lst1[i]+lst2[i])
	elif(lst1[i].isdigit() and lst2[i].isdigit()):
		result.append(int(lst1[i])+int(lst2[i]))
	else:
		result.append(float(lst1[i])+float(lst2[i]))
result=result+extra
print('The required resultant list is as follows:',result)


		

