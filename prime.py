#to find the prime numbers between two user-input numbers(both inclusive)
x=int(input('Enter the first number:'))
y=int(input('Enter the second number:'))
print('Prime numbers in range (',x,'-',y,') are as follows:',end=' ')
d=1
if x>y: d=-1
div=0
for i in range(x,y+1,d):
    div=0
    for j in range(1,i+1):
        if(i%j==0):
            div+=1
    if(div==2): print(i,end=' ')