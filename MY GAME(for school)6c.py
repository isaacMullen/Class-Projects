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
    countdown(1)
    print('[New Zone Discovered],fOrEsT oF tHe DeAd')
    print('''You arrive at the Inn, located in the middle of the FoReSt. You approach an old man, sitting by the mailbox.
It's unsettlingly dark and the air is occupied only by the noise of crows, They seem to be nervous over your arrival...''')

interact(playerCharacter, oldMan)

print('My name is not sir. It is Deccard. Address me by my name to continue talking')

oldMan = 'Deccard'

address = (input('type "excuse me, Deccard" to interact with the old man:'))

if (address == "excuse me, Deccard"):
    print('[Deccard] It is I, Deccard cain. What brings you to this vile, infested forest?')

choice = int(input('''enter 1 to tell the truth
enter 2 to lie: '''))


if (choice == 1):
    print('I have been sent by a squadrent located about 5 hours in that direction, you point south')
    print('[Deccard] Ah yes, you must be',playerCharacter,',we couldn\'t be in more dire need of your help than we are now, we\'re being overrun by the undead')
    print('[you] That is indeed my name, I am ready to begin my adventure at once')
    print('[Deccard] wonderful, tell me when you want to start')
    startAdventure = (input('type "begin" to embark on your adventure'))
elif(choice == 2):
    print('I wandered off my path on the way home and now now i\'ve ended up here')
    print('[Deccard] Well if you\'re willing to stay and help us with the undead, I will reward you handsomely')
    print('[you] I,',playerCharacter,', shall stay and help aid you in your efforts, I am always up for an adventure')
    print('[Deccard] wonderful, tell me when you\'re prepared to start')
    startAdventure = (input('type "begin" to embark on your adventure'))

if (startAdventure == 'begin'):
    print('''[daggers] ¤=[]:::::>
¤=[]:::::>''')
    print('''[wand + book] ━━━★
 ___
|   |
| M |
|___|''')
    print('[sword] ¤==[]::::::::::::>')
    print('[staff] 0===========O')
    print(input('which weapon do you prefer?: '))


                





    
   

       

