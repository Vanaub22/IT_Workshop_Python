#Python program to create a dictionary and do the following: a)sort dictionary by key b)sort dictionary by value
D={}
while(True):
    print('Enter items of the dictionary in key:value format:')
    temp=input().split(':')
    D[temp[0]]=temp[1]
    ch=int(input('Press 0 to exit OR 1 to continue:'))
    if(ch==0):
        break
print('User-input dictionary is as follows:',D)
sort_value_dict={}
sort_key_dict={}
for i in sorted(D.values()):
    for j in D.keys():
        if(D[j]==i):
            sort_value_dict[j]=i
for i in sorted(D.keys()):
    for j in D.values():
        if(D[i]==j):
            sort_key_dict[i]=j
print('The Dictionary sorted by values is as follows:',sort_value_dict)
print('The Dictionary sorted by keys is as follows:',sort_key_dict)