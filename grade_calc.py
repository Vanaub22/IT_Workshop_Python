#To creat a grade calculator
student={}
student['Name']=input('Enter the name of the student:')
def enterMarks():
    x=[]
    m=[]
    x=input().split(',')
    for i in x:
        if(not(i.isdigit())):
            m.append(float(i))
        else:
            m.append(int(i))
    return(m)
print('Enter the Assignment scores of',student['Name'],'separated by commas:',end=' ')
student['Assignments']=enterMarks()
print('Enter the Test scores of',student['Name'],'separated by commas:',end=' ')
student['Test']=enterMarks()
print('Enter the Lab Test scores of',student['Name'],'separated by commas:',end=' ')
student['Lab']=enterMarks()
print('Student database for',student['Name'],'is as follows:',student)
def avg(lst):
    sum,count=0,0
    for i in lst:
        count+=1
        sum+=i
    return(sum/count)
final_score=((70/100)*avg(student['Test']))+((20/100)*avg(student['Lab']))+((10/100)*avg(student['Assignments']))
print('Final average marks of',student['Name'],'is:',final_score)
print('Letter grade of',student['Name'],'is:',end='')
if(final_score>=90.0):
    print('A')
elif(final_score>=80.0 and final_score<=90.0):
    print('B')
elif(final_score>=70.0 and final_score<=80.0):
    print('C')
else:
    print('D')