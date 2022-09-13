#To write a Python function to find the Maximum of three numbers
L=[]
def max_of_three(a,b,c):
    if(a>b):
        if(a>c):return(a)
        else:return(c)
    else:
        if(b>c):
            return(b)
        else:
            return(c)
L=input('Enter three numbers separated by spaces:').split()
print(L)
print('The maximum number is:',max_of_three(int(L[0]),int(L[1]),int(L[2])))