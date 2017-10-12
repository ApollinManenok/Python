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


#           Proverka otveta da-net
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


'''#           Vyvod pravil
def rules(etap):
    if (etap == 'main'):
        print('RULES: ')
    elif (etap == ' '):
        print(' ')
    else:
        print(' ')


#          Join the game
<<<<<<< HEAD
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
=======
def join_the_game(players, money):
    while (True):
        name = input('\nEnter your name, please:  ')
        if(name in money):
            print('\nThis name already taken.  ')
        else:
            ans = input('\nYour name is '+name+', correctly? (Yes/No)  ')
            if(yes_no(ans)):
                cash = checking(input('\nHow much you want to bring in the game?  '))
                while(type(cash)!=int or cash<5):
                    if (type(cash) != int):
                        cash = checking(input('\nWrong enter. Try again:  '))
                    elif(cash<1):
                        cash = checking(input('\nYou need to bring in something. How much you are ready to bring in the game?  '))
                    else:
                        if(yes_no(input('\n'+name+'... Lets be honest, it\'s not enough to play.\nMaybe you have more? (Yes/No) '))):
                            cash = checking(input('\nHow much you are ready to bring in the game?   '))
                        else:
                            print('\nWell... No is no.')
                            cash = 0
                            break
                if (cash == 0):
                    print('\nYou can\'t join the game without money. Come back again later. \n\n')
                    break
                if(yes_no(input('\nOkey. Lets check... Your name is '+name+' and you bring in '+str(cash)+' points, correctly? (Yes/No) '))):
                    players.append(name)
                    money[name] = cash
                    print('\nNow you\'re in the game! Congratulations!\n')
                    if(yes_no(input('\nDoes anyone else want to join? (Yes/No) '))):
                        continue
>>>>>>> origin/master
                    else:
                        break
<<<<<<< HEAD
            if (money == 0):
                print('You can\'t join the game without money. Come back again later. ')
                break
            ##players.append(name)
                    
                    
            #cash(name)
            break
        else:
            name = input('\nEnter your name again, please  ')
    #
=======
                else:       
                    continue
            else:
                print('\nTry again, please.   ')
    return players, money
>>>>>>> origin/master


#          Leave the game
def leave_the_game(players, money):
    while(True):
        name = input('\nTell me who wan\'t to leave the game, please:  ')
        if(name in money):
            if(yes_no(input('\n'+name+' want to leave, correctly? (Yes/No)  '))):
                players.pop(name)
                money.pop(name)
                if(yes_no(input('\nDoes anyone else want to leave? (Yes/No) '))):
                    continue
                else:
                    break
            else:
                print('\nTry again, please.')
        else:
            print('\nThere is no such player.  ')
    return players, money'''
            


##################################################################################
#                                     MAIN
##################################################################################
players = list()
money = dict()

#bet ставка 
<<<<<<< HEAD
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
=======

>>>>>>> origin/master

while(True):
    menu = checking(input ('WELCOME to BLACKJACK GAME!\n\nMenu:\nPress 1 to read RULES.\nPress 2 to join the game.\nPress 3 to leave the game.\nPress 4 to start the game.\nPress 5 to exit game.\n\nEnter here:   '))
    if(type(menu)!=int or menu > 5 or menu < 1):
        print('\nWrong enter. Try again. ')
    elif(menu == 1):
        #rules('main')
        print('RULES: ')
    elif(menu == 2):
        #players, money = join_the_game(players, money)
        while (True):
            if(len(players) > 7):
                print('There are too much players already, you need to wait while someone leave the game. Sorry. \n')
                break
            else:
                name = input('\nEnter your name, please:  ')
                if(name in money):
                    print('\nThis name already taken.  ')
                else:
                    ans = input('\nYour name is '+name+', correctly? (Yes/No)  ')
                    if(yes_no(ans)):
                        cash = checking(input('\nHow much you want to bring in the game?  '))
                        while(type(cash)!=int or cash<5):
                            if (type(cash) != int):
                                cash = checking(input('\nWrong enter. Try again:  '))
                            elif(cash<1):
                                cash = checking(input('\nYou need to bring in something. How much you are ready to bring in the game?  '))
                            else:
                                if(yes_no(input('\n'+name+'... Lets be honest, it\'s not enough to play.\nMaybe you have more? (Yes/No) '))):
                                    cash = checking(input('\nHow much you are ready to bring in the game?   '))
                                else:
                                    print('\nWell... No is no.')
                                    cash = 0
                                    break
                        if (cash == 0):
                            print('\nYou can\'t join the game without money. Come back again later. \n\n')
                            break
                        if(yes_no(input('\nOkey. Lets check... Your name is '+name+' and you bring in '+str(cash)+' points, correctly? (Yes/No) '))):
                            players.append(name)
                            money[name] = cash
                            print('\nNow you\'re in the game! Congratulations!\n')
                            if(yes_no(input('\nDoes anyone else want to join? (Yes/No) '))):
                                continue
                            else:
                                break
                        else:       
                            continue
                    else:
                        print('\nTry again, please.   ')
    elif(menu == 3):
        #players, money = leave_the_game(players, money)
        while(True):
            if(len(players) < 1):
                print('There are no more players. \n')
                break
            else:
                name = input('\nTell me who wan\'t to leave the game, please:  ')
                if(name in money):
                    if(yes_no(input('\n'+name+' want to leave, correctly? (Yes/No)  '))):
                        players.pop(name)
                        money.pop(name)
                        if(yes_no(input('\nDoes anyone else want to leave? (Yes/No) '))):
                            continue
                        else:
                            break
                    else:
                        print('\nTry again, please.')
                else:
                    print('\nThere is no such player.  ')
    elif(menu == 4):
        #game
        while(True):
            #print(len(players))
            deck_amount = checking(input('Enter amount card decks (1 - 4)   '))
            if (type(deck_amount) != int):
                print('\nWrong enter\n')
            elif(deck_amount > 4 or deck_amount < 1):
                print('Can\'t use more than four decs or less than one ')
            deck = [2,3,4,5,6,7,8,9,10,11]*4*deck_amount
            shuffle(deck)
            
            
            break
    elif(menu == 5):
        print('Good bye! Come back again. ')
        break


# Vybor kol-va kolod dl'a igry 1,2,4

<<<<<<< HEAD

=======
"""
>>>>>>> origin/master
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
"""
