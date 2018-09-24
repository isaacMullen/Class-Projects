import random
import library
import time
from threading import Thread

playerChoice = None

library.countdown(1)

a = random.randint(0,4)

print('the computer chose',library.choices[a])

Thread(target = library.check).start()

playerChoice = (input('enter rock, paper, scissors, lizard or spock: '))


#player choosing rock, paper, scissors, lizard or spock.
while (playerChoice != 'rock' and playerChoice != 'paper' and playerChoice != 'scissors' and playerChoice != 'lizard' and playerChoice != 'spock'):
    print('please enter your selection correctly')
    playerChoice = (input('enter rock, paper, scissors, lizard or spock: '))

library.outcome(playerChoice, a)












