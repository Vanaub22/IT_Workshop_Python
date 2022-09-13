#to print the sum where N number of integer arguments are passed to a function make_sum()
def make_sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print('The sum of 2,3,4,5 and 6 is as follows:',make_sum(2,3,4,5,6))
print('The sum of -1,-2,-3 and 6 is as follows:',make_sum(-1,-2,-3,6))