start = int (input ('enter a start number: '))
difference  = int (input ('enter a difference number: '))
total = int (input('enter the amount of numbers you\'d like: '))
finalTotal = 0
for x in range(start, (total * difference + start), difference):
    finalTotal = finalTotal + x
print(finalTotal)

    
    


