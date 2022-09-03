#python program to Replace words from Dictionary
D={}
str=''
str=input('Enter the test string:')
str_lst=str.split(' ')
print('The user-input string is as follows:',str)
while(True):
    print('Enter items of the lookup dictionary in key:value format:')
    temp=input().split(':')
    D[temp[0]]=temp[1]
    ch=int(input('Press 0 to exit OR 1 to continue:'))
    if(ch==0):
        break
for i in range(len(str_lst)):
    if(str_lst[i] in D.keys()):
        str_lst[i]=D[str_lst[i]]
str=''
for i in str_lst:
    str+=(i+' ')
print('The final string after replacing is as follows:',str)