#to find the sum of two tuples using exception handling wherever necessary
def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
def isInteger(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
def custom_sum(a,b):
    if(isInteger(a) and isInteger(b)):
        return(int(a)+int(b))
    elif ((isFloat(a) and isInteger(b)) or (isFloat(b) and isInteger(a)) or (isFloat(a) and isFloat(b))):
        return(float(a)+float(b))
    else:
        return(a+b)
T1=tuple(input('Enter the elements of the first tuple separated by spaces:').split())
T2=tuple(input('Enter the elements of the second tuple separated by spaces:').split())
if(len(T1)>len(T2)):
    T1,T2=T2,T1
T3=[]
for i in range(len(T2)):
    try:
        T3.append(custom_sum(T1[i],T2[i]))
    except IndexError:
        T3.append(T2[i])
T3=tuple(T3)
print('The resultant tuple is as follows:',T3)

