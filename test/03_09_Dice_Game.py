# Igra v kosti
# dve kosti
# tri rezhima igry (odin igrok, dva igroka, igra s kompom)
#stavki na ugadannujy summu kostej, ili na pobedu
# vybor rezhima, opisanie pravil
from random import *


print('Welcome to the DICE GAME!\n')
#odin igrok
mode=1
point=0
answer=1
while(mode!=0):
    mode=int(input('Choose game mode:\nPress 1 if one player\nPress 2 if two players\nPress 3 if player whith computer\nPress 0 if you want to quit\n\nYour choice '))
    if(mode == 0):
        print('\nThank you for playing!')        
    elif(mode == 1):
        name = input('\nYou selected one player mode\nPlease, enter your name ')
        print('\nGlad to meet you,', name)
        print('\nRULES:\n1.In one player mode you need to guess the outcome of the roll\n(sum of two dices)\n2.In the begining you will enter amount of your points.\n3.Right before guessing you enter your bet.\nAfter each right guess you get your bet back plus equal amount of points.\nAfter each wrong - lose your bet.\n4.When your points will turn less or equal zero game will be over.\n5.If you want to quit the game before total lose just press 0.\n')
        while(point<=0):
            point = int(input('Enter points amount '))
        print('\n'+name+'\'s points: ', point,'\nWe are ready to start\n')
        while(answer!=0 and point>0):
            dice_one = randrange(1,7)
            dice_two = randrange(1,7)
            outcome = dice_one+dice_two
            bet=int(input('Enter your bet '))
            while(bet==0 or point-bet<0):
                if(bet==0):
                    bet=int(input('Your bet is zero, there is no sense, please, enter your bet '))
                if(point-bet<=0):
                    bet=int(input('Your bet is too big, you can\'t afford it. Try again. '))
            answer = int(input('Enter your guess '))
            while(answer<2 or answer>12):
                print('\n'+name+', outcome can\'t be less then 2 or bigger than 12. ')
                answer = int(input('Please, enter your guess again '))
            print('\n',dice_one,'...',dice_two,'   Outcome:',outcome)
            if (answer == outcome):
                print(outcome,':',answer, 'Congratulations, ',name,'! You win. +',bet,' points.\n')
                point += bet
            else:
                print(outcome,':',answer, 'Sorry, ',name,'. You lose. -',bet,' points.\n')
                point -= bet
            if(point<=0):
                print('Sorry, this game is over. Better luck next time!\n\n')
                break
            print('\n'+name+'\'s points: ',point)
    elif(mode == 2):
        print('\nYou selected two players mode')
    elif(mode == 3):
        print('\nYou selected player with computer mode')
    else:
        print('\nYou entered something wrong, try again -_-')



    

