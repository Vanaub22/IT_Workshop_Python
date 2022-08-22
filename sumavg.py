#to accept integer input until user enters zero and then calculate sum and average
print('The program will accept integers until 0 is entered.')
sum=0
n=0
while(True):
    i=int(input('Enter any number or else press 0 to exit:'))
    if(i==0):
        break
    sum+=i
    n+=1
avg=sum/n
print('The sum of the entered values =',sum)
print('The average of the values entered =',avg)
print('Execution Terminated')