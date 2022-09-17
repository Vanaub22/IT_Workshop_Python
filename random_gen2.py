import random as rd
import datetime as dt
print('A Random integer between 0 and 6(excluding 6) is:',rd.randint(0,5))
print('A Random integer between 0 and 10(excluding 10) is:',rd.randint(0,9))
print('A Random integer between 0 and 10 in step of 3 is as follows',rd.randrange(0,9,3))
date=list(map(int,input('Enter the first date in dd-mm-yyyy format:').split('-')))
date1=dt.date(date[2],date[1],date[0])
date=list(map(int,input('Enter the second date in dd-mm-yyyy format:').split('-')))
date2=dt.date(date[2],date[1],date[0])
Rdate=date1+dt.timedelta(days=rd.randrange((date2-date1).days))
print('A Random date between the two user-input dates is: {}-{}-{}'.format(Rdate.strftime('%d'),Rdate.strftime('%m'),Rdate.strftime('%Y')))