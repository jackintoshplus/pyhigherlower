#Higher or Lower
#
#Application created by Jack Herbert - 1/29/2023

#Library import
import random

#Application value declarations
activeGame = True;
wins = 0;

#Application greeter
print('Higher or Lower\n')

#Main application loop
while activeGame:

    #Set player values and reset locks.
    resetCheckActive = True;
    compareCheckActive = True;
    userInputCheckActive = True;
    usernum = 0
    battlenum = random.randint(1,100)

    #Application begins
    print('Prepare to battle! Current wins:', wins)
    print('Choose a number between 1 and 100.\n')

    #User input    
    while(userInputCheckActive):       
        try:
            usernum = input('Number: ')
            usernum = int(usernum)
        except ValueError:
            print("Invalid entry. Please try again.")
            continue

        if((usernum <= 0) or (usernum > 100)):
            print("Your number is not between 1 and 100. Please try again.")
        else:
            userInputCheckActive = False;

    #User Higher or Lower check
    while(compareCheckActive):
        usercompare = input('Will it be Higher or Lower:')      
        usercompare.lower 

        if((usercompare == 'higher') or (usercompare == 'lower')):
            compareCheckActive = False
        else:
            print("Invalid entry. Please try again")
            
    #User comparisons/Battle
    print('You believe', usernum, 'is', usercompare, 'than', battlenum)
    
    if((usernum > battlenum and usercompare == 'higher') or (usernum < battlenum and usercompare == 'lower')):
        print('You won!')
        wins += 1
    else:
        print('You lost...')

    #Re-lock reset game checker
    resetCheckActive = True;

    #Allow user to replay game or exit
    while resetCheckActive:
        resetCheck = input('Play again? (Y/N):')

        if((resetCheck == 'y')) or (resetCheck == 'n'):
            resetCheckActive = False
        else:
            print("Invalid entry. Please try again")

quit();
