import random
import time

SLEEP_BETWEEN_ACTIONS = 0.5

def checkRules(user):
    print('This is a game of Rock, Paper and Scissors')
    print('')
    userRules = input('Do you know the rules of the game? ')
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    var = userRules.lower()
    if var == 'yes':
        straightinto = print(f"Okay lets get straight into the game {user}")
        print('')
    elif var == 'no':
        print('')
        insert = print('Insert rules here')
    elif var != 'yes' or 'no':
        fuck = input('Fuckwit, its a yes or no question stupid fucking nigger: ')

def user():
    player = input('Please enter your username: ')
    print('')
    return player

def startGame():
    player1 = user()
    options = ['Rock', 'Paper', 'Scissors']
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    checkRules(player1)
    compScore = 0
    playerScore = 0
    print('Type Quit to quit at anytime: ')
    print('')
    while True:
        try:
            usersChoice = int(input('Please select from the following: 1:ROCK 2:PAPER 3:SCISSORS '))
            compChoice = random.choice(options)
        except ValueError:
            print('Fucking Shit Game NIgger')

        if usersChoice == 1 and compChoice == 'Scissors':
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(f"You have choosen... 'ROCK'")
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(f"The Computer has choosen... {compChoice}")
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print('YOU WIN!')
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            playerScore += 1
            print(f"Your score is now {playerScore}")
            time.sleep(SLEEP_BETWEEN_ACTIONS)

        elif usersChoice == 1 and compChoice == 'Paper':
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(f"You have choosen... ROCK")
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(f"The Computer has choosen... {compChoice}")
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print('YOU LOSE SHITTER!')
            compScore += 1
            print(f"Computers score is now {compScore}")
            time.sleep(SLEEP_BETWEEN_ACTIONS)

        elif usersChoice == 1 and compChoice == 'Scissors':
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(f"You have choosen... ROCK")
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(f"The Computer has choosen... {compChoice}")
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print('It is a draw')

        elif usersChoice == 2 and compChoice == 'Scissors':
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(f"You have choosen... PAPER")
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(f"The Computer has choosen... {compChoice}")
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print('YOU LOSE SHITTER!')
            compScore += 1
            print(f"Computers score is now {compScore}")
            time.sleep(SLEEP_BETWEEN_ACTIONS)

        elif usersChoice == 2 and compChoice == 'Rock':
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(f"You have choosen... PAPER")
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(f"The Computer has choosen... {compChoice}")
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print('YOU WIN!')
            playerScore += 1
            print(f"Your score is now {compScore}")
            time.sleep(SLEEP_BETWEEN_ACTIONS)

        elif usersChoice == 2 and compChoice == 'Paper':
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(f"You have choosen... PAPER")
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(f"The Computer has choosen... {compChoice}")
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print('It is a draw')

        elif usersChoice == 3 and compChoice == 'Rock':
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(f"You have choosen... Scissors")
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(f"The Computer has choosen... {compChoice}")
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print('YOU LOSE SHITTER!')
            compScore += 1
            print(f"Computers score is now {compScore}")
            time.sleep(SLEEP_BETWEEN_ACTIONS)

        elif usersChoice == 3 and compChoice == 'Paper':
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(f"You have choosen... Scissors")
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(f"The Computer has choosen... {compChoice}")
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print('YOU WIN!')
            playerScore += 1
            print(f"Your score is now {compScore}")
            time.sleep(SLEEP_BETWEEN_ACTIONS)

        elif usersChoice == 3 and compChoice == 'Scissors':
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(f"You have choosen... Scissors")
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(f"The Computer has choosen... {compChoice}")
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print('It is a draw')

startGame()
