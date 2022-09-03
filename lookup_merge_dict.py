#To create two dictionaries find keys of the first in the second and then merge the dictionaries
D1={}
D2={}
Df={}
def Enter_dict():
    D={}
    while(True):
        print('Enter items in key:value format:')
        temp=input().split(':')
        D[temp[0]]=temp[1]
        ch=int(input('Press 0 to exit OR 1 to continue:'))
        if(ch==0):
            break
    return(D)
print('Enter the items of Dictionary 1')
D1=Enter_dict()
print('Enter the items of Dictionary 2')
D2=Enter_dict()
print('User-input dictionary 1 is as follows:',D1)
print('User-input dictionary 2 is as follows:',D2)
while(True):
    k=input('Enter the key in Dictionary 1 to be searched for in Dictionary 2:')
    if(k in D1.keys()):
        break
    else:
        print(k,'is not a key in Dictionary 1...Try Again')
if(k not in D2.keys()):
    print('The key',k,'is not present in Dictionary 2')
else:
    print('The corresponding value in Dictionary 2 is',D2[k])
for i in D1.keys():
    for j in D2.keys():
        if(i==j):
            Df[i]=[D1[i],D2[i]]
for i in D1.keys():
    if(i in Df.keys()):
        continue
    else:
        Df[i]=D1[i]
for i in D2.keys():
    if(i in Df.keys()):
        continue
    else:
        Df[i]=D2[i]
print('The Merged Dictionary is as follows:',Df)
