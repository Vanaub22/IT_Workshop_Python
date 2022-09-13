#To Write a Python function to multiply all the numbers in a list
L=[]
def multList(lst):
    res=1
    for i in lst:
        res*=i
    return(res)
print('Enter the numbers in the list')
while(True):
    x=input('Enter a number or press Enter to Exit:')
    if(not(x=='')):
        L.append(int(x))
    else:
        print('Input terminated')
        break
print('The user-input list is as follows:',L)
print("Result after multiplying all the elements in the list is",multList(L))