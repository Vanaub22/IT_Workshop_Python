#To Swap two user-input tuples in Python
lst=[]
tuple1=tuple2=()
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
print('Enter the items of the first tuple.')
tuple1=Enter()
print('Enter the items of the second tuple.')
tuple2=Enter()
print('User-input tuple 1 is as follows:',tuple1)
print('User-input tuple 2 is as follows:',tuple2)
tuple1,tuple2=tuple2,tuple1
print('After swapping the tuples...')
print('New tuple 1 is as follows:',tuple1)
print('New tuple 2 is as follows:',tuple2)