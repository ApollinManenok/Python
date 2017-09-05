# Igra v kosti
# dve kosti
# tri rezhima igry (odin igrok, dva igroka, igra s kompom)
#stavki na ugadannujy summu kostej, ili na pobedu
# vybor rezhima, opisanie pravil
from random import *

def checking (var):
    try:
        var=int(var)
    except: TypeError
    return var
print('Welcome to the DICE GAME!\n')

mode=1
point=0
point_one=0
point_two=0
answer=1
computer_point=100000

# Vybor rezhima igry
while(mode!=0):
    mode=checking(input('\nChoose game mode:\nPress 1 if one player\nPress 2 if two players\nPress 3 if player and computer\nPress 0 if you want to quit\n\nYour choice '))
    while(type(mode)!=int or mode>3 or mode<0):
        mode = checking(input('\nYou entered something wrong, try again -_- '))

    if(mode == 0):
        print('\nThank you for playing!')
        break
    
# Odin igrok______________________________________________________________
    elif(mode == 1):
        name = input('You selected one player mode\nPlease, enter your name ')
        print('\nGlad to meet you,', name,'.')
        print('\nRULES:\n1.In one player mode you need to guess the outcome of the roll\n(sum of two dices)\n2.In the begining you will enter amount of your points.\n3.Right before guessing you enter your bet.\nAfter each right guess you get your bet back plus equal amount of points.\nAfter each wrong - lose your bet.\n4.When your points will turn less or equal zero game will be over.\n5.If you want to quit the game before total lose just press 0 at any time.\n')
        point = checking(input('Enter points amount '))
        while(type(point)!=int or point<0):
            if(type(point)!=int):
                point = checking(input('You entered not a number. Please, enter zero if you want to quit\nor enter points amount correctly '))
            else:
                point = checking(input('Points amount can\'t be less than zero. Please, enter zero if you want to quit\nor enter points amount correctly '))
        if (point == 0):
            print('\n'+name+', you left the game before the beginning.')
            again = input('Do you want to start again?(Yes/No)')
            while(True):
                if(again == 'Yes' or again == 'Да' or again == 'y' or again == 'yes' or again == 'Y' or again == 'Ye' or again == 'e' or again == 'Eah' or again == 'E' or again == 'Yap' or again == 'Канеш' or again == 'канеш' or again == 'угу' or again == 'ага' or again == 'ес'):
                    break
                elif(again == 'No' or again == 'Nea' or again == 'Net' or again == 'nea' or again == 'no' or again == 'net' or again == 'Нет' or again == 'нет' or again == 'Неа' or again == 'неа' or again == 'неть' or again == 'Неть' or again == 'низачто' or again == 'ни в коем случае' or again == 'уйди противный' or again == 'Уйди, противный' or again == 'Бебебе' or again == 'N' or again == 'n'):
                    print('You left the game. Good by!')
                    break
                else:
                    again = input('Sorry, wrong value. Enter again do you want to start again?(Yes/No) ')
        
        print('\n'+name+'\'s points: ', point,'\nWe are ready to start\n')

#Start igry s odnim igrokom

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
            else:
                again = input('Sorry, wrong value. Enter again do you want to start again?(Yes/No) ')
            
        print('\n'+name+'\'s points: ', point,'\nComputer points: ', computer_point,'\nWe are ready to start\n')

# Nevernyj vvod________________________________________________
    #else:
     #   mode =checking(input('\nYou entered something wrong, try again -_- '))
      #  continue

# Cikl igry ____________________________________________________
    

input()


    

