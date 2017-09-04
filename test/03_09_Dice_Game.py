# Igra v kosti
# dve kosti
# tri rezhima igry (odin igrok, dva igroka, igra s kompom)
#stavki na ugadannujy summu kostej, ili na pobedu
# vybor rezhima, opisanie pravil
from random import *


print('Welcome to the DICE GAME!\n')

mode=1
point=0
point_one=0
point_two=0
answer=1
computer_point=100000

# Vybor rezhima igry
while(mode!=0):
    mode=int(input('\nChoose game mode:\nPress 1 if one player\nPress 2 if two players\nPress 3 if player and computer\nPress 0 if you want to quit\n\nYour choice '))

    if(mode == 0):
        print('\nThank you for playing!')
    
# Odin igrok______________________________________________________________
    elif(mode == 1):
        name = input('\nYou selected one player mode\nPlease, enter your name ')
        print('\nGlad to meet you,', name,'.')
        print('\nRULES:\n1.In one player mode you need to guess the outcome of the roll\n(sum of two dices)\n2.In the begining you will enter amount of your points.\n3.Right before guessing you enter your bet.\nAfter each right guess you get your bet back plus equal amount of points.\nAfter each wrong - lose your bet.\n4.When your points will turn less or equal zero game will be over.\n5.If you want to quit the game before total lose just press 0.\n')
        point = int(input('Enter points amount '))
        while(point<0):
            point = int(input('Points amount can\'t be less than zero. Enter zero if you want to quit or enter points amount correctly '))
        if (point == 0):
            print('\n'+name+', you left the game before the beginning.')
            again = input('Do you want to start again?(Yes/No)')
            if(again == 'Yes' or again == 'Да' or again == 'y' or again == 'yes' or again == 'Y' or again == 'Ye' or again == 'e' or again == 'Eah' or again == 'E' or again == 'Yap' or again == 'Канеш' or again == 'канеш' or again == 'угу' or again == 'ага' or again == 'ес'):
                continue
            elif(again == 'No' or again == 'Nea' or again == 'Net' or again == 'nea' or again == 'no' or again == 'net' or again == 'Нет' or again == 'нет' or again == 'Неа' or again == 'неа' or again == 'неть' or again == 'Неть' or again == 'низачто' or again == 'ни в коем случае' or again == 'уйди противный' or again == 'Уйди, противный' or again == 'Бебебе' or again == 'N' or again == 'n'):
                print('You left the game. Good by!')
                break
        
        print('\n'+name+'\'s points: ', point,'\nWe are ready to start\n')

#Dva igroka__________________________________________________________________
    elif(mode == 2):
        print('\nYou selected two players mode')
        name_one = input('\nPlease, enter first player name ')
        name_two = input('\nPlease, enter second player name ')
        print('\nGlad to meet you, '+name_one+' and '+name_two+'.')
        print('\nRULES:\n1.In two players mode you need to guess the outcome of the roll\n(sum of two dices)\n2.In the begining both of you will enter amount of your points.\n3.Right before guessing first player enter his(her) bet, then second player do the same.\n4.Then players make their guessing, and the winner take it all or both lose.\n5.When points of one of the players will turn less or equal zero game will be over.\n6.If any player want to quit the game before total lose just press 0 at any time.\n')

# Ochki pervogo
        point_one = int(input('Enter points amount for first player '))
        while(point_one<0):
            point_one = int(input('Points amount can\'t be less than zero. Enter zero if you want to quit or enter points amount correctly '))
        if (point_one == 0):
            print('\n'+name_one+' left the game before the beginning.Traitor!\n')
            again = input('Do you want to start again?(Yes/No) ')
            if(again == 'Yes' or again == 'Да' or again == 'y' or again == 'yes' or again == 'Y' or again == 'Ye' or again == 'e' or again == 'Eah' or again == 'E' or again == 'Yap' or again == 'Канеш' or again == 'канеш' or again == 'угу' or again == 'ага' or again == 'ес'):
                continue
            elif(again == 'No' or again == 'Nea' or again == 'Net' or again == 'nea' or again == 'no' or again == 'net' or again == 'Нет' or again == 'нет' or again == 'Неа' or again == 'неа' or again == 'неть' or again == 'Неть' or again == 'низачто' or again == 'ни в коем случае' or again == 'уйди противный' or again == 'Уйди, противный' or again == 'Бебебе' or again == 'N' or again == 'n'):
                print('You left the game. Good by!')
                break
            else:
                again = input('Sorry, wrong value. Enter again do you want to start again?(Yes/No) ')

# Ochki vtorogo
        point_two = int(input('Enter points amount for second player '))
        while(point_two<0):
            point_two = int(input('Points amount can\'t be less than zero. Enter zero if you want to quit or enter points amount correctly '))
        if (point_one == 0):
            print('\n'+name_two+' left the game before the beginning. Traitor!\n')
            again = input('Do you want to start again?(Yes/No) ')
            if(again == 'Yes' or again == 'Да' or again == 'y' or again == 'yes' or again == 'Y' or again == 'Ye' or again == 'e' or again == 'Eah' or again == 'E' or again == 'Yap' or again == 'Канеш' or again == 'канеш' or again == 'угу' or again == 'ага' or again == 'ес'):
                continue
            elif(again == 'No' or again == 'Nea' or again == 'Net' or again == 'nea' or again == 'no' or again == 'net' or again == 'Нет' or again == 'нет' or again == 'Неа' or again == 'неа' or again == 'неть' or again == 'Неть' or again == 'низачто' or again == 'ни в коем случае' or again == 'уйди противный' or again == 'Уйди, противный' or again == 'Бебебе' or again == 'N' or again == 'n'):
                print('You left the game. Good by!')
                break
            else:
                again = input('Sorry, wrong value. Enter again do you want to start again?(Yes/No) ')
                
        print('\n'+name_one+'\'s points: ', point_one,'\n'+name_two+'\'s points: ', point_two,'\nWe are ready to start\n')

#Igra s kompom_____________________________________________________________
    elif(mode == 3):
        name = input('\nYou selected player and computer mode\nPlease, enter your name ')
        print('\nGlad to meet you,', name,'.')
        print('\nRULES:\n1.In player and computer mode you need to guess the outcome of the roll (sum of two dices)\n2.In the begining you will enter amount of your points. Computer points are', computer_point, '\n3.Right before guessing you enter your bet, computer do the same.\n4. Then both do their guessing and the winner take it all or both lose.\n5.When your points will turn less or equal zero game will be over.\n6.If you want to quit the game before total lose just press 0 at any time.\n')
        point = int(input('Enter points amount '))
        while(point<0):
            point = int(input('Points amount can\'t be less than zero. Enter zero if you want to quit or enter points amount correctly '))
        if (point == 0):
            print('\n'+name+', you left the game before the beginning.')
            again = input('Do you want to start again?(Yes/No)')
            if(again == 'Yes' or again == 'Да' or again == 'y' or again == 'yes' or again == 'Y' or again == 'Ye' or again == 'e' or again == 'Eah' or again == 'E' or again == 'Yap' or again == 'Канеш' or again == 'канеш' or again == 'угу' or again == 'ага' or again == 'ес'):
                continue
            elif(again == 'No' or again == 'Nea' or again == 'Net' or again == 'nea' or again == 'no' or again == 'net' or again == 'Нет' or again == 'нет' or again == 'Неа' or again == 'неа' or again == 'неть' or again == 'Неть' or again == 'низачто' or again == 'ни в коем случае' or again == 'уйди противный' or again == 'Уйди, противный' or again == 'Бебебе' or again == 'N' or again == 'n'):
                print('You left the game. Good by!')
                break
        
        print('\n'+name+'\'s points: ', point,'\nComputer points: ', computer_point,'\nWe are ready to start\n')
        
#Nevernyj vvod____________________________________________________________
    else:
        print('\nYou entered something wrong, try again -_-')
        continue

# Cikl igry    
    while(answer!=0):
        dice_one = randrange(1,7)
        dice_two = randrange(1,7)
        outcome = dice_one+dice_two
        bet=int(input('Enter your bet '))
        while(point-bet<0):
            bet=int(input('Your bet is too big, you can\'t afford it. Try again. '))
        if(bet==0):
                print('\n'+name+', you left the game. Your points are ', point)
                again = input('Do you want to start again?(Yes/No)')
                if(again == 'Yes' or again == 'Да' or again == 'y' or again == 'yes' or again == 'Y' or again == 'Ye' or again == 'e' or again == 'Eah' or again == 'E' or again == 'Yap' or again == 'Канеш' or again == 'канеш' or again == 'угу' or again == 'ага' or again == 'ес'):
                    continue
                elif(again == 'No' or again == 'Nea' or again == 'Net' or again == 'nea' or again == 'no' or again == 'net' or again == 'Нет' or again == 'нет' or again == 'Неа' or again == 'неа' or again == 'неть' or again == 'Неть' or again == 'низачто' or again == 'ни в коем случае' or again == 'уйди противный' or again == 'Уйди, противный' or again == 'Бебебе' or again == 'N' or again == 'n'):
                    print('You left the game. Good by!')
                    break
        answer = int(input('Enter your guess '))
        while(answer<2 or answer>12):
            if(answer == 0):
                break
            print('\n'+name+', outcome can\'t be less then 2 or bigger than 12. If you want to quit press zero.')
            answer = int(input('Please, enter your guess again '))
        if (answer == 0):
                print('\n'+name+', you left the game. Your points are ', point)
                again = input('Do you want to start again?(Yes/No)')
                if(again == 'Yes' or again == 'Да' or again == 'y' or again == 'yes' or again == 'Y' or again == 'Ye' or again == 'e' or again == 'Eah' or again == 'E' or again == 'Yap' or again == 'Канеш' or again == 'канеш' or again == 'угу' or again == 'ага' or again == 'ес'):
                    continue
                elif(again == 'No' or again == 'Nea' or again == 'Net' or again == 'nea' or again == 'no' or again == 'net' or again == 'Нет' or again == 'нет' or again == 'Неа' or again == 'неа' or again == 'неть' or again == 'Неть' or again == 'низачто' or again == 'ни в коем случае' or again == 'уйди противный' or again == 'Уйди, противный' or again == 'Бебебе' or again == 'N' or again == 'n'):
                    print('You left the game. Good by!')
                    break
            
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

input()


    

