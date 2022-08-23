#To take a list as input, separate the items based on type and store them in 3 different lists, sort and display
lst=[]
floatlst=[]
stringlst=[]
intlst=[]
while(True):
    n=int(input('Enter the number of items in the list(minimum 8):'))
    if(n<8):
        print('Mnimum number of items should be 8...Try Again')
    else:
        break
for i in range(n):
    print('Enter the item',i+1,':',end=' ')
    lst.append(input())
print('User-input list is as follows:',lst)
def isFloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
def isInteger(x):
    try:
        int(x)
        return True
    except ValueError:
        return False
for i in lst:
    if(isInteger(i)):
        intlst.append(int(i))
    elif(isFloat(i)):
        floatlst.append(float(i))
    else:
        stringlst.append(i)
print('The unsorted string list is as follows:',stringlst)
print('The unsorted integer list is as follows:',intlst)
print('The unsorted floating point number list is as follows:',floatlst)
stringlst.sort(reverse=True)
floatlst.sort(reverse=True)
intlst.sort(reverse=True)
print('AFTER SORTING IN DESCENDING ORDER:')
print('The sorted string list in descending order is as follows:',stringlst)
print('The sorted integer list in descending order is as follows:',intlst)
print('The sorted floating point number list in descending order is as follows:',floatlst)