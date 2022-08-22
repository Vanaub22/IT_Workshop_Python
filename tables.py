#create a multiplication table using while loop
i=1
num=int(input('Enter the number:'))
print('Multiplication Table for',num,':')
while(i<=10):
  print(num,'x',i,'=',num*i)
  i+=1