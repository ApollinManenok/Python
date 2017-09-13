# Igra v kosti

#################### IMPORT #######################

from random import *

###################################################




######################     FUNCTIONS     #########################


########    Функция сключения ошибки ввода и вылета программы    ########

def checking (var):
    try:
        var=int(var)
    except: TypeError
    return var


########    Функция рестарта    ########

def restart(again):
    while(True):
        if(again == 'Yes' or again == 'Да' or again == 'y' or again == 'yes' or again == 'Y'
           or again == 'Ye' or again == 'e' or again == 'Eah' or again == 'E' or again == 'Yap'
           or again == 'Канеш' or again == 'канеш' or again == 'угу' or again == 'ага' or again == 'ес'
           or again=='Да!' or again=='ДА' or again=='!' or again=='!!!' or again=='--' or again=='+'
           or again=='ляляля' or again=='Ляляля' or again=='start' or again=='давай' or again=='Давай'):
            return 1
        elif(again == 'No' or again == 'Nea' or again == 'Net' or again == 'nea' or again == 'no'
           or again == 'net' or again == 'Нет' or again == 'нет' or again == 'Неа' or again == 'неа'
           or again == 'неть' or again == 'Неть' or again == '-' or again == 'ни в коем случае'
           or again == 'уйди противный' or again == 'Уйди, противный' or again == 'Бебебе'
           or again == 'N' or again == 'n' or again == '0' or again=='нетушки' or again=='н' or again=='Н'
           or again=='ненене' or again=='Ненене' or again=='НЕТ' or again=='Надоело' or again=='надоело'):
            print('You left the game. Good bye!')
            return 0
        else:
            again = input('Sorry, wrong value. Enter again do you want to start again?(Yes/No) ')


########    Ставка компьютера   ########

def counting(comp_point, bet):
    mn = 1
    num = bet
    while(num//10!=0):
        num = num//10
        mn*=10
    while(True):
        var=int(randrange(bet-mn//2-1,bet+mn//2)+1)
        if(comp_point-var<0):
            if(comp_point<10):
                var = comp_point
            else:
                var = comp_point//2
                break
        elif(var>0):
            break
    return var


########    Проверка имени    ########

def namme(name):
    while(name==''):
        name=input('You need a name or nickname or something... How we can call you? ')
    return name

            
########    Проверка на ввод очков игрока   ########

def points(point):
    point = checking(point)
    while(type(point)!=int or point<0):
        if(type(point)!=int):
            point = checking(input('You entered not a number. Please, enter zero if you want to quit \nor enter points amount correctly '))
        else:
            point = checking(input('Points amount can\'t be less or equal zero. Please, enter zero if you want to quit\nor enter points amount correctly '))
    return point

########    Проверка на ввод ставки игрока    ########
            
def bett(point, bet):
    if (bet == 'vabank' or bet=='all' or bet=='ALL' or bet=='All' or bet=='Всё' or bet=='Все' or bet=='всё'
        or bet=='все' or bet=='вабанк' or bet=='Вабанк' or bet=='Vabank' or bet=='Vse' or bet=='vse'):
        bet = point
        print('Your bet:', bet)
        return bet
    bet=checking(bet)
    while(type(bet)!=int or point-bet<0 or bet<0):
        if(type(bet)!=int):
            bet=checking(input('Wrong enter. Try again. '))
        elif(bet<0):
            bet=checking(input('Bet can\'t be less than one. Try again. '))
        else:
            bet=checking(input('Your bet is too big, you can\'t afford it. Try again. '))    
    return bet


########    Проверка на ввод ответа игрока    ########

def answerr(name, answer):
    answer=checking(answer)
    while(type(answer)!=int or answer<2 or answer>12):
        if(type(answer)!=int):
            answer = checking(input('Wrong enter. Try again. '))
        elif(answer == 0):
            break
        else:
            print('\n'+name+', outcome can\'t be less then 2 or bigger than 12.\nIf you want to quit press zero.')
            answer = checking(input('Please, enter your guess again '))
    return answer


########    Funkcija igry s odnim igrokom    ########

def game_one(point, name):
    answer=1   #переменная для хранения загаданного числа игроком
    while(answer!=0):
        dice_one = randrange(1,7)
        dice_two = randrange(1,7)
        outcome = dice_one+dice_two
       
# Stavka i ee proverka vmeste s vyhodom
        bet=bett(point,input('\nEnter your bet '))
        if(bet==0):
            print('\n'+name+', you left the game. Your points are ', point)
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): return 1
            else: return 0
        point-=bet
        
# Otvet i ego proverka vmeste s vyhodom
        answer = answerr(name, input('Enter your guess '))
        if (answer == 0):
            print('\n'+name+', you left the game. Your points are ', point)
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): return 1
            else: return 0

        input('\nPress Enter when you are ready...')
        
        
# Sravnenie                
        print('\n',dice_one,'...',dice_two,'    Outcome:',outcome, name+'\'s answer:',answer)
        if (answer == outcome):
            print('\nCongratulations, '+name+'! You win. +',bet,' points.\n')
            point += bet*2
        else:
            print('\nSorry, '+name+'. You lose.\n')

        input('\nPress Enter when you are ready...')
                
# Proverka ochkov
        if(point<=0):
            print('\nSorry, you lose all your points, so this game is over.\nBetter luck next time!\n')
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): return 1
            else: return 0
        print('\n'+name+'\'s points: ',point)


########    Funkcija igry s dvum'a igrokami    ########
        
def game_two(point_one, point_two, name_one, name_two):
    answer1=1  # переменная для хранения
    answer2=1  # загаданного числа игроками
    while(answer1!=0 and answer2!=0):
        dice_one = randrange(1,7)   # 1 kost'
        dice_two = randrange(1,7)   # 2 kost'
        outcome = dice_one+dice_two # rezul'tat kostej

# Stavka i otvet pervogo. Proverka vmeste s vyhodom
        print('\n'+name_one+'\'s turn.\n')       
      
        bet1=bett(point_one, input('Enter your bet '))
        if(bet1==0):
            print('\n'+name_one+', you left the game. Your points are', point_one, name_two+' points are', point_two)
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): return 1
            else: return 0
        point_one-=bet1
        
        answer1 = answerr(name_one, input('Enter your guess '))
        if (answer1 == 0):
            print('\n'+name_one+', you left the game. Your points are ', point_one, name_two+' points are', point_two)
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): return 1
            else: return 0

# Stavka i otvet vtorogo. Proverka vmeste s vyhodom            
        print('\n'+name_two+'\'s turn.\n')
        
        bet2=bett(point_two,input('Enter your bet '))
        if(bet2==0):
            print('\n'+name_two+', you left the game. Your points are', point_two, name_one+' points are', point_one)
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): return 1
            else: return 0
        point_two-=bet2
        
        answer2 = answerr(name_two, input('Enter your guess '))
        if (answer2 == 0):
            #print('Are you shure you want to quit? You will lose your bet ')
            print('\n'+name_two+', you left the game. Your points are', point_two, name_one+' points are', point_one)
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): return 1
            else: return 0

        input('\nPress Enter when you are ready...')
        
# Sravnenie                
        print('\n',dice_one,'...',dice_two,'    Outcome:',outcome,'   '+name_one+'\'s answer:',answer1,'   '+name_two+'\'s answer:', answer2)
        if(answer2==outcome and answer1 == outcome):
            print('\nBoth of you guessed right '+name_one+' and '+name_two+'!\nYou get +',(bet1+bet2)//2,' points.\n')
            point_one+=(bet1+bet2)//2
            point_two+=(bet1+bet2)//2
        elif(answer1 == outcome):
            print('\nCongratulations, '+name_one+'! You win. +',bet1+bet2,' points.\nSorry, '+name_two+'. You lose.\n')
            point_one += bet1+bet2
        elif(answer2 == outcome):
            print('\nCongratulations, '+name_two+'! You win. +',bet1+bet2,' points.\nSorry, '+name_one+'. You lose.\n')
            point_two += bet1+bet2
        else:
            print('\nSorry, '+name_one+' and '+name_two+'. You both lose.\n')

        input('\nPress Enter when you are ready...')
        
        
# Proverka ochkov
        if(point_one<=0 or point_two<=0):
            if(point_one<=0 and point_two<=0):
                print('Sorry, this game is over for both of you '+name_one+' and '+name_two+'.\n Better luck next time!\n')
            elif(point_two<=0):
                print('Sorry, this game is over for '+name_two+'. Better luck next time!\n')
            else:
                print('Sorry, this game is over for '+name_one+'. Better luck next time!\n')
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): return 1
            else: return 0
                
        print('\n'+name_one+'\'s points: ', point_one,'\n'+name_two+'\'s points: ', point_two)


########    Funkcija igry igroka s computerom    ########

def game_computer(comp_point, point, name):
    answer=1  # переменная для хранения загаданного числа игроком
    comp_answer=1 # otvet compa
    while(answer!=0):
        dice_one = randrange(1,7)   # 1 kost'
        dice_two = randrange(1,7)   # 2 kost'
        outcome = dice_one+dice_two # rezul'tat kostej

# Stavka i otvet igroka. Proverka vmeste s vyhodom
        print('\n'+name+'\'s turn.\n')       

        bet=bett(point, input('Enter your bet '))
        if(bet==0):
            print('\n'+name+', you left the game. Your points are', point, 'Computer points are', comp_point)
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): return comp_point+1
            else: return comp_point*(-1)
        point-=bet
        
        answer = answerr(name, input('Enter your guess '))
        if (answer == 0):
            print('\n'+name+', you left the game. Your points are ', point, 'Computer points are', comp_point)
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): return comp_point+1
            else: return comp_point*(-1)
            
# Stavka i otvet compa
        print('\nComputer turn.\n')
        
        comp_bet=counting(comp_point, bet)
        comp_point-=comp_bet
        comp_answer = randrange(2,12)
        print('Bet:',comp_bet,'\nAnswer',comp_answer,'\n\n')
        input('Press Enter when you are ready...')
        
# Sravnenie                
        print('\n',dice_one,'...',dice_two,'  Outcome:',outcome,'   '+name+'\'s answer:',answer, '    Computer answer:', comp_answer)
        if(answer==outcome and comp_answer == outcome):
            print('\nBoth of you guessed right '+name+' and Computer!\nYou get +',(bet+comp_bet)//2,' points.\n')
            point+=(bet+comp_bet)//2
            comp_point+=(bet+comp_bet)//2
        elif(answer == outcome):
            print('\nCongratulations, '+name+'! You win. +',bet+comp_bet,' points.\nComputer lose.\n')
            point += bet+comp_bet
        elif(comp_answer==outcome):
            print('\nComputer win! +',bet+comp_bet,' points.\nSorry, '+name+'. You lose.\n')
            comp_point += bet+comp_bet
        else:
            print('\n'+name+' and Computer both lose.\n')
        input('\nPress Enter when you are ready...')
        
# Proverka ochkov
        if(point<=0 or comp_point<=0):
            if(point<=0):
                print('Sorry, this game is over for '+name+'. Better luck next time!\n')
            elif(comp_point<=0):
                print('Computer points are zero... We lose... \nHow is that possible! \n\nNoooooooooooooooooo!\n\n\n',
                      'Well... you can\'t play with Computer any longer!\nBye bye! ^-^')
            else:
                print('Sorry, this game is over for both, '+name+' and Computer.\n Better luck next time!\n')
                input('\n')
                input('Wait! Computer points are zero... We lose... \nHow is that possible! \n\nNoooooooooooooooooo!\n\n\n')
                input('Well... you can\'t play with Computer any longer!\nBye bye! ^-^')
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): return comp_point+1
            else: return comp_point*(-1)
                
        print('\n'+name+'\'s points: ', point,'\nComputer points: ', comp_point)
        


            
########################     НАЧАЛО ИГРЫ. MAIN.     ########################################

print('Welcome to the DICE GAME!\n')

mode=1            # режим игры
point=0           # объявление переменной для подсчёта очков в одиночной игре и игре против компа
point_one=0       # объявление переменной для подсчёта очков первого игрока в игре для двух игроков
point_two=0       # объявление переменной для подсчёта очков второго игрока в игре для двух игроков
comp_point=100000 # очки компьютера


########      Vybor rezhima igry     ########

while(mode!=0):  # Основной цикл с проверкой на ввод
    print('\nChoose game mode:\nPress 1 if one player\nPress 2 if two players\n'+
          'Press 3 if player and computer\nPress 0 if you want to quit')
    mode=checking(input('\n\nYour choice '))
    while(type(mode)!=int or mode>3 or mode<0):
        mode = checking(input('\nYou entered something wrong, try again -_- '))
        
# Vyhod iz igry
    if(mode == 0):
        print('\nThank you for playing!')
        break


########   Odin igrok    ########
    
    elif(mode == 1):
        
# Vvod imeni s proverkoj na vyhod
        name = namme(input('You selected one player mode\nPlease, enter your name '))
        if(name=='0'):
            print('\nYou left the game before the beginning.')
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): continue
            else:break
        print('\nGlad to meet you, '+name+'.')
        print('\nRULES:\n1.In one player mode you need to guess the outcome of the roll\n(sum of two dices)\n'+
              '2.In the begining you will enter amount of your points.\n'+
              '3.Right before guessing you enter your bet. After each right guess you get your\n'+
              'bet back plus equal amount of points. After each wrong lose your bet.\n'+
              '4.When your points will turn less or equal zero game will be over.\n'+
              '5.If you want to quit the game before total lose just press 0 at any time.\n')
        
# Vvod ochkov s proverkoj na vvod i vyhod
        point = points(input('Enter points amount '))
        if (point == 0):
            print('\n'+name+', you left the game before the beginning.')
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): continue
            else:break
        print('\n'+name+'\'s points: ', point,'\nWe are ready to start.\n')
        input('\nPress Enter when you are ready...')
        
# Vyzov funkcii igry dl'a odnogo
        stop = game_one(point, name)
        if(stop == 1): continue
        else:break


########    Dva igroka    #########
        
    elif(mode == 2):
        print('\nYou selected two players mode')
        
# Vvod imen s proverkoj na vyhod
        name_one = namme(input('\nPlease, enter first player name '))
        if(name_one=='0'):
            print('\nYou left the game before the beginning.')
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): continue
            else:break            
        name_two = namme(input('\nPlease, enter second player name '))
        if(name_two=='0'):
            print('\nYou left the game before the beginning.')
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): continue
            else:break            
        print('\nGlad to meet you, '+name_one+' and '+name_two+'.')
        print('\nRULES:\n1.In two players mode you need to guess the outcome of the roll\n(sum of two dices)'+
              '\n2.In the begining both of you will enter amount of your points.\n'+
              '3.Right before guessing first player enter his(her) bet, then second player\ndo the same.\n'+
              '4.Then players make their guessing, and the winner take it all or both lose.\n'+
              '5.When points of one of the players will turn less or equal zero game will\nbe over.\n'+
              '6.If any player want to quit the game before total lose just press 0 at any time\n')
        
# VVod ochkov s proverkoj na vyhod
        point_one = points(input('Enter points amount for first player '))
        if (point_one == 0):
            print('\n'+name_one+', you left the game before the beginning. Traitor!')
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): continue
            else:break
        point_two = points(input('Enter points amount for second player '))
        if (point_two == 0):
            print('\n'+name_two+', you left the game before the beginning. Traitor!')
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): continue
            else:break                
        print('\n'+name_one+'\'s points: ', point_one,'\n'+name_two+'\'s points: ', point_two,'\nWe are ready to start.\n')
        input('\nPress Enter when you are ready...')
        
#Vyzov funkcii igry s dvum'a igrokami
        stop = game_two(point_one, point_two, name_one, name_two)
        if(stop == 1): continue
        else:break


########    Igra s kompom    ########

    elif(mode == 3):

# Proverka na vozmozhnost' igry s compom.
        if(comp_point <= 0):
            print('You can\'t choose this mode. Computer points are equal zero.\nWe are very VERY VEERYY SORRRYYYY!!!! X_X')
            continue
        
# Vvod imeni s proverkoj na vyhod
        name = namme(input('\nYou selected player and computer mode\nPlease, enter your name '))
        if(name=='0'):
            print('\nYou left the game before the beginning.')
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): continue
            else:break
        print('\nGlad to meet you, '+name+'.')                
        print('Rules:\n1.In player and computer mode you need to quess the outcome of\nthe roll '+
              '(sum of two dices).\n2.First of all you need to enter amount of your points.\n'+
              'Computer points at the moment are', comp_point,'\n'+
              '3.Before guessing you enter your bet, then computer do the same.\n'+
              '4.Next thing your guessing will be checked and the winner take it all or you\nboth lose.\n'+
              '5.If your or computer points will turn less or equal zero game will be over.\n'+
              '6.If you want to quit the game before total lose just press 0 at any time.\n')
        
# Vvod ochkov s proverkoj na vvod i vyhod
        point = points(input('Enter points amount '))
        if (point == 0):
            print('\n'+name+', you left the game before the beginning.')
            stop = restart(input('Do you want to start again?(Yes/No) '))
            if(stop == 1): continue
            else:break
        print('\n'+name+'\'s points: ', point,'Computer\'s points:', comp_point, '\nWe are ready to start\n')
        input('\nPress Enter when you are ready...')
        
# Vyzov funkcii igry dl'a igry s kompom
        stop = game_computer(comp_point, point, name)
        if(stop > 0):
            comp_point = stop-1
            continue
        else:
            comp_point = stop*(-1)
            break

input()
