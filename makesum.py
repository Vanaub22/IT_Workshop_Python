#to print the sum where N number of integer arguments are passed to a function make_sum()
def make_sum(*args):
    lst=list(*args)
    print('The required sum is:',sum(lst))
make_sum(list(map(int,input('Enter the numbers separated by spaces: ').split())))