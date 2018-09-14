import secrets

#figure out what beats what.
def playerWins(i, j):
    print(i,' wins')

def playerLoses(i, j):
    print(j,' wins')

def playerTie(i,j):
    (i , j,'ties')
playerChoice = (input('enter rock, paper, scissors, lizard or spock: '))
rock = playerChoice
paper = playerChoice
scissors = playerChoice
lizard = playerChoice
spock = playerChoice

pcChoice = ['rock', 'paper', 'scissors', 'lizard', 'spock']
print('the computer chose',secrets.choice(pcChoice))


if (playerChoice == 'rock' and (pcChoice == 'paper' or pcChoice == 'spock' or pcChoice ==)):
    playerLoses (playerChoice, pcChoice)
    
