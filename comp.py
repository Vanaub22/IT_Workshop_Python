#to compare 2 user-input numbers
x=int(input('Enter the first number: '))
y=int(input('Enter the second number: '))
if(x>y):
	print('The first number is greater than the second number.')
elif(y>x):
	print('The second number is greater than the first number.')
else:
	print('The two numbers are equal.')
