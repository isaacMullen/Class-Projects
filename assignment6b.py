aminoAcidWeight = 0
weightOxygen = 15.9994
weightNitrogen = 14.00674
weightHydrogen = 1.00794
weightCarbon = 12.011
weightSulfur = 32.066

def add(oxygen, sulfur, carbon, hydrogen, nitrogen):
    aminoAcidWeight = (oxygen * weightOxygen) + (sulfur * weightSulfur) + (carbon * weightCarbon) + (hydrogen * weightHydrogen) + (nitrogen * weightNitrogen)
    print('amino acid weight is: ', aminoAcidWeight)

numOxygen = int(input('enter the number of Oxygen atoms you\'d like: '))
numSulfur = int(input('enter the number of Sulfur atoms you\'d like: '))
numCarbon = int(input('enter the number of Carbon atoms you\'d like: '))
numHydrogen = int(input('enter the number of Hydrogen atoms you\'d like: '))
numNitrogen = int(input('enter the number of Nitrogen atoms you\'d like: '))

add(numOxygen, numSulfur, numCarbon, numHydrogen, numNitrogen)









