#let user input their own 2 numbers and add all numbers in between
y = 0
z = 0
while (True):
    y = int (input ('enter your first number'))
    if (y == 1234567890):
        break
    z = int (input ('enter your second number'))
    num = 0
    for x in range(y,(z+1)):
        num = num + x
    print ('number is',num)
print ('you got out')
    


