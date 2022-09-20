import random as rd
import string as st
lst=list(map(int,input('Enter two integers for generation of random numbers between them(both inclusive):').split()))
print('The random integer generated is as follows:',rd.randint(lst[0],lst[1]))
print('The random multiple of 7 between 0 and 70 is as follows:',(7*rd.randint(0,10)))
Rstr=''
for i in range(30):
	Rstr=Rstr+rd.choice(st.ascii_letters) 
print('The random string generated is as follows:',Rstr)
