# To accept 3 strings from the user, search for the second string within the first string and replace with the third string
original=input('Enter the first string: ')
str=input('Enter the second string: ')
newstr=input('Enter the third string: ')
new=original.replace(str,newstr)
print('The new string after replacing: ',new)


