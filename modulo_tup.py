#To input two tuples and find Modulo of corresponding tuple elements and store in a third tuple
lst=[]
mod_tup=tuple1=tuple2=()
def Enter():
	i=0
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
	return(tup)
print('Enter the items of the first tuple:')
tuple1=Enter()
print('Enter the items of the second tuple:')
tuple2=Enter()
print('The first tuple is: ',tuple1)
print('The second tuple is: ',tuple2)
if(len(tuple1)!=len(tuple2)):
    print('The tuples are not of equal length')
else:
    for i in range(len(tuple1)):
        lst.append(int(tuple1[i])%int(tuple2[i]))
    mod_tup=tuple(lst)
    print('The tuple containing the modulo values is as follows:',mod_tup)