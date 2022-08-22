#To Copy specific elements from one tuple to a new tuple
lst=[]
tuple1=tuple2=()
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
tuple1=tuple(lst)
lst.clear()
print('User-input tuple is as follows:',tuple1)
print('Enter the items to be copied:')
i=0
while(True):
    i+=1
    print('Enter the item',i,'or press Enter to Exit:',end=' ')
    x=input()
    if(x!='' and x in tuple1):
        lst.append(x)
    elif(x!='' and x not in tuple1):
        print(x,'is not an item in the initial tuple...Try Again')
        i-=1
    else:
        print('Input terminated')
        break
tuple2=tuple(lst)
print('Required new tuple having copied items: ',tuple2)