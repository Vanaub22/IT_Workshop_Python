#To Write a Python function that accepts a string and calculates the number of uppercase and lowercase letters
def case_count():
    lower,upper=0,0
    str=input('Enter the string:')
    for i in range(len(str)):
            if(str[i].isupper()):
                upper+=1
            if(str[i].islower()):
                lower+=1
    print('User-input string is as follows:',str)
    print('The number of Uppercase characters:',upper)
    print('The number of Lowercase characters:',lower)
case_count()
