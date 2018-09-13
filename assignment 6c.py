import secrets
playerChoice = (input('enter rock, paper, scissors, lizard or spock: '))
rock = playerChoice
paper = playerChoice
scissors = playerChoice
lizard = playerChoice
spock = playerChoice

pcChoice = ['rock', 'paper', 'scissors', 'lizard', 'spock']
print(secrets.choice(pcChoice))

#figure out what beats what.
def playerWins(i, j):
    print(i,' wins')

def playerLoses(i, j):
    print(j,' wins')

def playerTie(i,j):
    (i , j,'ties')

if (playerChoice == rock and pcChoice == paper):
    playerWins (playerChoice, pcChoice)
    
