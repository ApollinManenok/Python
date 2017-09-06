# Igra v kosti

######## IMPORT ###########

from random import *

###########################



######################     FUNCTIONS     #########################


########    Функция проверки ввода    ########

def checking (var):
    try:
        var=int(var)
    except: TypeError
    return var


########    Funkcija nachat' snachala    ########

def restart(again):
    while(True):
        if(again == 'Yes' or again == 'Да' or again == 'y' or again == 'yes' or again == 'Y'
           or again == 'Ye' or again == 'e' or again == 'Eah' or again == 'E' or again == 'Yap'
           or again == 'Канеш' or again == 'канеш' or again == 'угу' or again == 'ага' or again == 'ес'):
            return 1
        elif(again == 'No' or again == 'Nea' or again == 'Net' or again == 'nea' or again == 'no'
           or again == 'net' or again == 'Нет' or again == 'нет' or again == 'Неа' or again == 'неа'
           or again == 'неть' or again == 'Неть' or again == 'низачто' or again == 'ни в коем случае'
           or again == 'уйди противный' or again == 'Уйди, противный' or again == 'Бебебе'
           or again == 'N' or again == 'n' or again == '0'):
            print('You left the game. Good bye!')
            return 0
        else:
            again = input('Sorry, wrong value. Enter again do you want to start again?(Yes/No) ')


########    Vvod stavki    ########
            
def bett(point, bet):
    bet=checking(bet)
    while(type(bet)!=int or point-bet<0 or bet<0):
        if(type(bet)!=int):
            bet=checking(input('Wrong enter. Try again. '))
        elif(bet<0):
            bet=checking(input('Bet can\'t be less than one. Try again. '))
        else:
            bet=checking(input('Your bet is too big, you can\'t afford it. Try again. '))    
    return bet


########    Vvod otveta    ########

def answerr(name, answer):
    answer=checking(answer)
    while(type(answer)!=int or answer<2 or answer>12):
            if(type(answer)!=int):
                answer = checking(input('Wrong enter. Try again. '))
            elif(answer == 0):
                break
            else:
                print('\n'+name+', outcome can\'t be less then 2 or bigger than 12. If you want to quit press zero.')
                answer = checking(input('Please, enter your guess again '))
    return answer


########    Funkcija igry s odnim igrokom    ########

def game_one(point, name):
    answer=1   #переменная для хранения загаданного числа игроком
    while(answer!=0):
        dice_one = randrange(1,7)
        dice_two = randrange(1,7)
        outcome = dice_one+dice_two
       
      #Stavka i ee proverka vmeste s vyhodom
        bet=bett(point,input('Enter your bet '))
        if(bet==0):
            print('\n'+name+', you left the game. Your points are ', point)
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): return 1
            else: return 0
        point-=bet
        
      #otvet i ego proverka vmeste s vyhodom
        answer = answerr(name, input('Enter your guess '))
        if (answer == 0):
            print('\n'+name+', you left the game. Your points are ', point)
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): return 1
            else: return 0
      #sravnenie                
        print('\n',dice_one,'...',dice_two, '   Outcome:',outcome, '    '+ name+'\'s answer:',answer)
        if (answer == outcome):
            print('Congratulations, ',name,'! You win. +',bet,' points.\n')
            point += bet
        else:
            print('Sorry, ',name,'. You lose.\n')
            if(point<=0):
                print('Sorry, this game is over. Better luck next time!\n')
                stop = restart(input('Do you want to start again?(Yes/No) '))
                if(stop == 1): return 1
                else: return 0
        print('\n'+name+'\'s points: ',point)


########    Funkcija igry s dvum'a igrokami    ########
        
def game_two(point_one, point_two, name_one, name_two):
    answer1=1  # переменная для хранения
    answer2=1  # загаданного числа игроком
    while(answer1!=0 and answer2!=0):
        dice_one = randrange(1,7)   # 1 kost'
        dice_two = randrange(1,7)   # 2 kost'
        outcome = dice_one+dice_two # rezul'tat kostej

        print('\n'+name_one+'\'s turn:')       
      #Stavka pervogo i ee proverka vmeste s vyhodom
        bet1=bett(point_one, input('Enter your bet '))
        if(bet1==0):
            print('\n'+name_one+', you left the game. Your points are', point_one, name_two+' points are', point_two)
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): return 1
            else: return 0
        point_one-=bet1
        
      #otvet pervogo i ego proverka vmeste s vyhodom
        answer1 = answerr(name_one,input('Enter your guess '))
        if (answer1 == 0):
            print('\n'+name_one+', you left the game. Your points are ', point_one, name_two+' points are', point_two)
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): return 1
            else: return 0

        print('\n'+name_two+'\'s turn:')    
      #Stavka vtorogo i ee proverka vmeste s vyhodom
        bet2=bett(point_two,input('Enter your bet '))
        if(bet2==0):
            print('\n'+name_two+', you left the game. Your points are', point_two, name_one+' points are', point_one)
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): return 1
            else: return 0
        point_two-=bet2
        
      #otvet vtorogo i ego proverka vmeste s vyhodom
        answer2 = answerr(name_two, input('Enter your guess '))
        if (answer2 == 0):
            #print('Are you shure you want to quit? You will lose your bet ')
            print('\n'+name_two+', you left the game. Your points are', point_two, name_one+' points are', point_one)
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): return 1
            else: return 0

      #sravnenie                
        print('\n',dice_one,'...',dice_two,'  Outcome:',outcome, '    '+name_one+'\'s answer:',answer1, '    '+name_two+'\'s answer:', answer2)
        if (answer1 == outcome):
            print('Congratulations, '+name_one+'! You win. +',bet1+bet2,' points.\nSorry, '+name_two+'. You lose.\n')
            point_one += bet1+bet2
        elif(answer2==outcome):
            print('Congratulations, '+name_two+'! You win. +',bet1+bet2,' points.\nSorry, '+name_one+'. You lose.\n')
            point_two += bet1+bet2
        elif(answer2==outcome and answer1 == outcome):
            print('Both of you guessed right '+name_one+' and '+name_two+'!\nYou get +',(bet1+bet2)/2,' points.\n')
            point_one+=(bet1+bet2)/2
            point_two+=(bet1+bet2)/2
        else:
            print('Sorry, '+name_one+' and '+name_two+'. You both lose.\n')
        if(point_one<=0 or point_two<=0):
            if(point_one<=0):
                print('Sorry, this game is over for '+name_one+'. Better luck next time!\n')
            elif(point_one<=0):
                print('Sorry, this game is over for '+name_two+'. Better luck next time!\n')
            else:
                print('Sorry, this game is over for both of you '+name_one+' and '+name_two+'.\n Better luck next time!\n')
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): return 1
            else: return 0
                
        print(name_one+'\'s points: ', point_one,'\n'+name_two+'\'s points: ', point_two)
        
            
########################     НАЧАЛО ИГРЫ. ПРИВЕТСТВИЕ.     ########################################

print('Welcome to the DICE GAME!\n')

mode=1        #режим игры
point=0       #объявление переменной для подсчёта очков в одиночной игре и игре против компа
point_one=0   #объявление переменной для подсчёта очков первого игрока в игре для двух игроков
point_two=0   #объявление переменной для подсчёта очков второго игрока в игре для двух игроков
   
computer_point=100000# очки компьютера

#################      Vybor rezhima igry     ################

while(mode!=0):  # Основной цикл с проверкой на ввод
    mode=checking(input('\nChoose game mode:\nPress 1 if one player\nPress 2 if two players\nPress 3 if player and computer\nPress 0 if you want to quit\n\nYour choice '))
    while(type(mode)!=int or mode>3 or mode<0):
        mode = checking(input('\nYou entered something wrong, try again -_- '))

    if(mode == 0):
        print('\nThank you for playing!')
        break


#######################   Odin igrok    ##############################
    
    elif(mode == 1):
########  Vvod imeni s proverkoj na vyhod
        name = input('You selected one player mode\nPlease, enter your name ')
        if(name=='0'):
            print('\nYou left the game before the beginning.')
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): continue
            else:break
        print('\nGlad to meet you, '+name+'.')
        print('\nRULES:\n1.In one player mode you need to guess the outcome of the roll (sum of two dices)\n',
              '2.In the begining you will enter amount of your points.\n',
              '3.Right before guessing you enter your bet.\nAfter each right guess you get your ',
              'bet back plus equal amount of points.\nAfter each wrong - lose your bet.\n',
              '4.When your points will turn less or equal zero game will be over.\n',
              '5.If you want to quit the game before total lose just press 0 at any time.\n')
########  Vvod ochkov s proverkoj na vvod i vyhod
        point = checking(input('Enter points amount '))
        while(type(point)!=int or point<0):
            if(type(point)!=int):
                point = checking(input('You entered not a number. Please, enter zero if you want to quit\nor enter points amount correctly '))
            else:
                point = checking(input('Points amount can\'t be less than zero. Please, enter zero if you want to quit\nor enter points amount correctly '))
        if (point == 0):
            print('\n'+name+', you left the game before the beginning.')
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): continue
            else:break
        print('\n'+name+'\'s points: ', point,'\nWe are ready to start\n')
########  Vyzov funkcii igry dl'a odnogo
        stop = game_one(point, name)
        if(stop == 1): continue
        else:break


######################    Dva igroka    #################################
        
    elif(mode == 2):
        print('\nYou selected two players mode')
########  Vvod imen s proverkoj na vyhod
        name_one = input('\nPlease, enter first player name ')
        if(name_one=='0'):
            print('\nYou left the game before the beginning.')
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): continue
            else:break
        name_two = input('\nPlease, enter second player name ')
        if(name_two=='0'):
            print('\nYou left the game before the beginning.')
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): continue
            else:break
        print('\nGlad to meet you, '+name_one+' and '+name_two+'.')
        print('\nRULES:\n1.In two players mode you need to guess the outcome of the roll\n(sum of two dices)\n2.In the begining both of you will enter amount of your points.\n3.Right before guessing first player enter his(her) bet, then second player do the same.\n4.Then players make their guessing, and the winner take it all or both lose.\n5.When points of one of the players will turn less or equal zero game will be over.\n6.If any player want to quit the game before total lose just press 0 at any time.\n')

########  Ochki pervogo
        point_one = checking(input('Enter points amount for first player '))
        while(type(point_one)!=int or point_one<0):
            if(type(point_one)!=int):
                point_one = checking(input('You entered not a number. Please, enter zero if you want to quit\nor enter points amount correctly '))
            else:
                point_one = checking(input('Points amount can\'t be less than zero. Please, enter zero if you want to quit\nor enter points amount correctly '))
        if (point_one == 0):
            print('\n'+name_one+', you left the game before the beginning. Traitor!')
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): continue
            else:break
       
        
########  Ochki vtorogo
        point_two = int(input('Enter points amount for second player '))
        while(type(point_two)!=int or point_two<0):
            if(type(point_two)!=int):
                point_two = checking(input('You entered not a number. Please, enter zero if you want to quit\nor enter points amount correctly '))
            else:
                point_two = checking(input('Points amount can\'t be less than zero. Please, enter zero if you want to quit\nor enter points amount correctly '))
        if (point_two == 0):
            print('\n'+name_two+', you left the game before the beginning. Traitor!')
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): continue
            else:break
                
        print('\n'+name_one+'\'s points: ', point_one,'\n'+name_two+'\'s points: ', point_two,'\nWe are ready to start\n')
        stop = game_two(point_one, point_two, name_one, name_two)
        if(stop == 1): continue
        else:break

'''



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
'''    

input()


    

