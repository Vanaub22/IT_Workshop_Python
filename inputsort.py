# accept a list from the user having n elements the list may have integer or string values.
# do not accept the value n
# accept input until the user presses the enter key
# after creating the initial list store the integer values in a new list and the strings in another list
# now sort the lists in ascending order
# now swap the lists and print them
list=[]
i=0
while(True):
	i+=1;
	print('Enter the item',i,'or press Enter to Exit:',end=' ')
	x=input()
	if(x!=''):
		list.append(x)
	else:
		print('List terminated')
		break
print('User-input list is as follows:',list)
num_lst=[]
str_lst=[]
for j in list:
	if(j.isdigit()):
		num_lst.append(int(j))
	else:
		str_lst.append(j)
print('The separated string list:',str_lst)
print('The separated number list:',num_lst)
num_lst.sort()
str_lst.sort(key=str.lower)
temp=str_lst
str_lst=num_lst
num_lst=temp
print("String list(modified): ",str_lst)
print("Number list(modified): ",num_lst)
		

