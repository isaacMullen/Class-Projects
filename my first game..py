x = 67
print ('''Welcome to my game... You will be asked to choose a number between
1 and 100, The computer has also chosen a number between 1 and 100. The object
of this game is to eventually reach the same number as the computer. using
simple information you will be provided with in the form of <,>,=.''')
num1 = int(input('choose a number'))
print('your number is',num1)
while (num1 != x):
    if (num1 < x):
        print('more')
    if (num1 > x):
        print('less')
    num1 = int(input('choose a number'))
print('YOU WON')

    



