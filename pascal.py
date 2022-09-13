#To Write a Python function that prints out the first n rows of Pascal's triangle
def Pascal(n):
    for i in range(1, n+1):
        for j in range(0, n-i+1):
            print(' ', end='')
        C = 1
        for j in range(1, i+1):
            print(' ', C, sep='', end='')
            C = C * (i - j) // j
        print()
n=input("Enter the number of rows for which Pascal's Triangle is to be generated:")
Pascal(int(n))