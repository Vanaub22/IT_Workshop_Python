import math
h,r=list(map(float,input('Enter the height and the radius of the cylinder separated by spaces:').split()))
print('Volume of the cylinder = {}\nSurface Area of the cylinder = {}'.format((math.pi*pow(r,2)*h),(2*math.pi*r*(r+h))))