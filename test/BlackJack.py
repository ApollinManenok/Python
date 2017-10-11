##################################################################################
#                                   IMPORT                  
##################################################################################

from random import *


##################################################################################
#                                 FUNCTIONS
##################################################################################

#           Proverka vvoda
def checking (var):
    try:
        var=int(var)
    except: TypeError
    return var


#
def yes_no(answer):
    while(True):
        if(answer == 'Yes' or answer == 'Да' or answer == 'y' or answer == 'yes' or answer == 'Y'
           or answer == 'Ye' or answer == 'e' or answer == 'Eah' or answer == 'E' or answer == 'Yap'
           or answer == 'Канеш' or answer == 'канеш' or answer == 'угу' or answer == 'ага' or answer == 'ес'
           or answer=='Да!' or answer=='ДА' or answer=='!' or answer=='!!!' or answer=='--' or answer=='+'
           or answer=='ляляля' or answer=='Ляляля' or answer=='start' or answer=='давай' or answer=='Давай'):
            return 1
        elif(answer == 'No' or answer == 'Nea' or answer == 'Net' or answer == 'nea' or answer == 'no'
           or answer == 'net' or answer == 'Нет' or answer == 'нет' or answer == 'Неа' or answer == 'неа'
           or answer == 'неть' or answer == 'Неть' or answer == '-' or answer == 'ни в коем случае'
           or answer == 'уйди противный' or answer == 'Уйди, противный' or answer == 'Бебебе'
           or answer == 'N' or answer == 'n' or answer == '0' or answer=='нетушки' or answer=='н' or answer=='Н'
           or answer=='ненене' or answer=='Ненене' or answer=='НЕТ' or answer=='Надоело' or answer=='надоело'):
            return 0
        else:
            answer = input('Sorry, I don\'t understand. What would be your answer again?(Yes/No) ')


#           Vyvod pravil
def rules(etap):
    if (etap == 'main'):
        print('RULES: ')
    elif (etap == ''):
        print('')
    else:
        print()


#          Join the game
def join_the_game():
    name = input('\nEnter your name, please  ')
    while (True):
        ans = input('\nYour name is '+name+', correctly?')
        if(yes_no(ans)):
            money = checking(input('\nHow much you want to bring in the game?  '))
            while(type(money)!=int or money<5):
                if (type(money) != int):
                    money = checking(input('\nWrong enter. Try again. '))
                elif(money<1):
                    money = checking(input('\nYou need to bring in something. How much you are ready to bring in the game?  '))
                else:
                    if(yes_no(input('\n'+name+'... Lets be honest, it\'s not enough to play.\nMaybe you have more? (Yes/No) '))):
                        money = checking(input('\nHow much you are ready to bring in the game?  '))
                    else:
                        print('Well... No is no. ')
                        money = 0
                        break
            if (money == 0):
                print('You can\'t join the game without money. Come back again later. ')
                break
            ##players.append(name)
                    
                    
            #cash(name)
            break
        else:
            name = input('\nEnter your name again, please  ')
    #

    


##################################################################################
#                                     MAIN
##################################################################################
players = list()
money = dict()

#bet ставка 
while(True):
    menu = checking(input ('WELCOME to BLACKJACK GAME!\n\nMenu:\nPress 1 to read RULES.\nPress 2 to join the game.\nPress 3 to exit game.\n\n'))
    while(type(menu)!=int or ):
    if(type(menu)!=int):
        menu = checking(input('Wrong enter. Try again. '))
    elif(menu == 1):
        rules('main')
    elif(menu == 2):
        join_the_game()
    elif(menu == 3):
        print()
    else:
            print()



again = 'y'
while(again == 'y'):
    koloda = [2,3,4,6,7,8,9,10,11]*4
    shuffle(koloda)
    r1 = []
    r2 = []
    r1.append(koloda.pop())
    r2.append(koloda.pop())
    r1.append(koloda.pop())
    r2.append(koloda.pop())
    sum1 = sum(r1)
    sum2 = sum(r2)
    
    print('\nPlayer1\' turn:\nYour cards:',r1,'   Sum:',sum1)
    ans1 = input('Player1, do you need more? (y/n) ')
    while(ans1 != 'n'):
        if (ans1 == 'y'):
            r1.append(koloda.pop())
            sum1+=r1[len(r1)-1]
            print('\nYour cards:',r1,'   Sum:',sum1)
        elif(ans1 == 'n'):
            print('Your result is ', sum1)
            break
        else:
            ans1 = input('You entered something wrong, try again.\n\n Do you need more? (y/n) ')
        if(sum1>21):
            print('Too much!')
            break
        ans1 = input('Player1, do you need more? (y/n) ')
    print('\nPlayer2\' turn:\nYour cards:',r2,'   Sum:',sum2)
    ans2 = input('Player2, do you need more? (y/n) ')
    while(ans2 != 'n'):
        if (ans2 == 'y'):
            r2.append(koloda.pop())
            sum2+=r2[len(r2)-1]
            print('\nYour cards:',r2,'  Sum:',sum2)
        elif(ans2 == 'n'):
            print('Your result is ', sum2)
            break
        else:
            ans2 = input('You entered something wrong, try again.\n\nDo you need more? (y/n) ')
        if(sum2>21):
            print('Too much!')
            break
        ans2 = input('Player2, do you need more? (y/n) ')
    print('\nSum 1 = ', sum1,'Sum 2 = ',sum2,'\n')
    if(sum1 <= 21 and sum2 <= 21):
        if (sum1>sum2):
            print('Player1 win!')
        elif(sum2>sum1):
            print('Player2 win!')
        else:
            print('Tie!')
    else:
        if(sum1>21 and sum2>21):
            print('Tie!')
        elif(sum2>21):
            print('Player1 win!')
        else:
            print('Player2 win!')
    again = input('Do you want to play again? (y/n) ')
    if (again == 'y'):
        continue
    elif (again == 'n'):
        print('Bye-bye!')
        break
    else:
        while(again!='y' and again!='n'):
            again = input('Something wrong.\n\nDo you want to play again? (y/n) ')
