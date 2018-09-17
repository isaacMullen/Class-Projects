import random
import time
T = 5
def countdown(T) :
    while(T > 0):
        print(T)
        T = T - 1
        time.sleep(1)
        print(T)
        T = T - 1
        time.sleep(1)
        print(T)
        T = T - 1
        time.sleep(1)
        print(T)
        T = T - 1
        time.sleep(1)
        print(T)
        T = T - 1
        time.sleep(1)
        print(T)
        T = T - 1
        if T ==0:
            print ('you lose')
countdown(5)
#figure out what beats what.
def playerWins(i, j):
    print(i,' wins')

def playerLoses(i, j):
    print(j,' wins')

def playerTie(i,j):
    print(i , j,'ties')

playerChoice = (input('enter rock, paper, scissors, lizard or spock: '))

a=random.randint(0,4)
pcChoice = ['rock', 'paper', 'scissors', 'lizard', 'spock']
print('the computer chose',pcChoice[a])
#loses
if (playerChoice == 'rock' and (pcChoice[a] == 'paper' or pcChoice[a] == 'spock')):
    playerLoses (playerChoice, pcChoice[a])

elif (playerChoice == 'paper' and (pcChoice[a] == 'scissors' or pcChoice[a] == 'spock')):
    playerLoses (playerChoice, pcChoice[a])

elif (playerChoice == 'scissors' and (pcChoice[a] == 'spock' or pcChoice[a] == 'rock')):
    playerLoses (playerChoice, pcChoice[a])

elif (playerChoice == 'lizard' and (pcChoice[a] == 'scissors' or pcChoice[a] == 'rock')):
    playerLoses (playerChoice, pcChoice[a])
     
elif (playerChoice == 'spock' and (pcChoice[a] == 'paper' or pcChoice[a]== 'lizard')):
    playerLoses (playerChoice, pcChoice[a])
#wins
elif (playerChoice == 'rock' and (pcChoice[a] == 'scissors' or pcChoice[a]== 'lizard')):
    playerWins (playerChoice, pcChoice[a])

elif (playerChoice == 'paper' and (pcChoice[a] == 'rock' or pcChoice[a] == 'spock')):
    playerWins (playerChoice, pcChoice[a])

elif (playerChoice == 'scissors' and (pcChoice[a] == 'paper' or pcChoice[a] == 'lizard')):
    playerWins (playerChoice, pcChoice[a])

elif (playerChoice == 'lizard' and (pcChoice[a] == 'spock' or pcChoice[a] == 'paper')):
    playerWins (playerChoice, pcChoice[a])

elif (playerChoice == 'spock' and (pcChoice[a] == 'rock' or pcChoice[a] == 'scissors')):
    playerWins (playerChoice, pcChoice[a])
#ties
elif (playerChoice == 'rock' and (pcChoice[a] == 'rock')):
    playerTies (playerChoice, pcChoice[a])


elif (playerChoice == 'paper' and (pcChoice[a] == 'paper')):
    playerTies (playerChoice, pcChoice[a])

elif (playerChoice == 'scissors' and (pcChoice[a] == 'scissors')):
    playerTies (playerChoice, pcChoice[a])

elif (playerChoice == 'lizard' and (pcChoice[a] == 'lizard')):
    playerTies (playerChoice, pcChoice[a])

elif (playerChoice == 'spock' and (pcChoice[a] == 'spock')):
    playerTies (playerChoice, pcChoice[a])




