formula=list(map(str,input("Enter the formula: ").split()))
print(formula)
if len(formula)!=3:
   print("Wrong Input")
   raise ArithmeticError
try:
   formula[0]=float(formula[0])
   formula[2]=float(formula[2])
except ValueError:
   print("Wrong input value type")
   raise ArithmeticError
if formula[1]!='+' and formula[1]!='-':
   print("Wrong operation input")
   raise ArithmeticError
if formula[1]=='+':
   print((formula[0]+formula[2]))
else:
   print((formula[0]-formula[2]))

