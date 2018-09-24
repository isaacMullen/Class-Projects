import random
import time
import library
choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']

pcChoice = random.randint(0,4)
done=False
while (done==False):
    playerChoice = (input('enter rock, paper, scissors, lizard or spock: '))

    if (playerChoice != 'rock' and playerChoice != 'paper' and playerChoice !='scissors' and playerChoice !='lizard' and playerChoice !='spock'):
        print('what\'re you doing.....')
    else:
        done=True




print('the computer chose', choices[pcChoice])  
library.countdown(3,playerChoice,choices,pcChoice)





