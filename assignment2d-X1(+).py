import math
#let the user pick the numbers to insert into the quadratic formula
num1 = int (input ('please insert a number'))
num2 = int (input ('please insert a number'))
num3 = int (input ('please insert a number'))
#establish numbers, a=(1) b=(-2) c=(1)
a = num1
b = num2
c = num3
#calculate x intercept for (+)
X1 = float(-b+(((-b*-b)-(4*a*c))**0.5))/(2*a)
print ('X1 is',X1)
