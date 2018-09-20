import time

def countdown(T):
    while(T > 0):
        print(T)
        T = T - 1
        time.sleep(1)
        if T == 0:
            break
oldMan = 'sir'

def interact(i, j):
    talk = (input('type "talk" to interact with this person: '))
    if (talk == 'talk'):
        print('excuse me,', j)

playerCharacter = (input('what is your character\'s name?: '))

print('''welcome to the team''',playerCharacter,'''we have urgent business in fOrEsT oF tHe DeAd.
The undead wont slay themselves...''')

travel = (input('type "go" to travel to the fOrEsT oF tHe DeAd: '))


if (travel == 'go'):
    print('travel will commence in...')
    countdown(5)
    print('[New Zone Discovered],fOrEsT oF tHe DeAd')
    print('''You arrive at the Inn, located in the middle of the fOrEsT oF tHe DeAd. You approach an old man, sitting by the mailbox.
It's unsettlingly dark and the air is occupied only by the noise of crows, They seem to be nervous over your arival...''')

interact(playerCharacter, oldMan)

print('My name is not sir. It is Deccard. Address me by my name to continue talking')

oldMan = 'Deccard'

address = (input('type "excuse me, Deccard" to interact with the old man:'))

if (address == "excuse me, Deccard"):
    print('It is I, Deccard cain. What brings you to this vile, infested forest')





    
   

       

