import random
import time

#choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']

def playerWins():
    print('you win')

def playerLoses():
    print('you lose')

def playerTies():
    print('tie game')


#loses
def outcome(playerChoice,choices,pcChoice):
    if (playerChoice == 'rock' and (choices[pcChoice] == 'paper' or choices[pcChoice] == 'spock')):
        playerLoses()

    elif (playerChoice == 'paper' and (choices[pcChoice] == 'scissors' or choices[pcChoice] == 'spock')):
        playerLoses()

    elif (playerChoice == 'scissors' and (choices[pcChoice] == 'spock' or choices[pcChoice] == 'rock')):
        playerLoses()

    elif (playerChoice == 'lizard' and (choices[pcChoice] == 'scissors' or choices[pcChoice] == 'rock')):
        playerLoses()
         
    elif (playerChoice == 'spock' and (choices[pcChoice] == 'paper' or choices[pcChoice]== 'lizard')):
        playerLoses()
    #wins
    elif (playerChoice == 'rock' and (choices[pcChoice] == 'scissors' or choices[pcChoice]== 'lizard')):
        playerWins()

    elif (playerChoice == 'paper' and (choices[pcChoice] == 'rock' or choices[pcChoice] == 'spock')):
        playerWins()

    elif (playerChoice == 'scissors' and (choices[pcChoice] == 'paper' or choices[pcChoice] == 'lizard')):
        playerWins()

    elif (playerChoice == 'lizard' and (choices[pcChoice] == 'spock' or choices[pcChoice] == 'paper')):
        playerWins()

    elif (playerChoice == 'spock' and (choices[pcChoice] == 'rock' or choices[pcChoice] == 'scissors')):
        playerWins()
    #ties
    elif (playerChoice == 'rock' and (choices[pcChoice] == 'rock')):
        playerTies()

    elif (playerChoice == 'paper' and (choices[pcChoice] == 'paper')):
        playerTies()

    elif (playerChoice == 'scissors' and (choices[pcChoice] == 'scissors')):
        playerTies()

    elif (playerChoice == 'lizard' and (choices[pcChoice] == 'lizard')):
        playerTies()

    elif (playerChoice == 'spock' and (choices[pcChoice] == 'spock')):
        playerTies()

def countdown() :
    while(T > 0):
        print(T)
        T = T - 1
        time.sleep(1)
        if T ==0:
             
