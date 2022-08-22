#to find the factorial of user-input number
num=int(input('Enter the number:'))
if(num==0):
    print('The required factorial: 0! = 1')
    exit()
copy=num
fact=1
while(copy>0):
    fact*=copy
    copy-=1
print('The required factorial:',num,'! =',fact)