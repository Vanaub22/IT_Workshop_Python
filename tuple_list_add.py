#to Add Tuple to List and vice – versa
lst=[]
tup=()
i=0
print('Enter the items of the tuple:')
while(True):
    i+=1
    print('Enter the item',i,'or press Enter to Exit:',end=' ')
    x=input()
    if(x!=''):
        lst.append(x)
    else:
        print('Input terminated')
        break
tup=tuple(lst)
lst.clear()
i=0
print('Enter the items of the list:')
while(True):
	i+=1
	print('Enter the item',i,'or press Enter to Exit:',end=' ')
	x=input()
	if(x!=''):
		lst.append(x)
	else:
		print('Input terminated')
		break
print('User-input tuple is as follows:',tup)
print('User-input list is as follows:',lst)
newlst=lst+list(tup)
tup+=tuple(lst)
print('The new tuple after adding list items: ',tup)
print('The new list after adding tuple items: ',newlst)
