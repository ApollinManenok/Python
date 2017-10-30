####   Tamagochi game

################################################################################
#                                          IMPORT                  
################################################################################


from random import *
from myobjectmodule import *
from critter_pics import *
import os
import time


################################################################################
#                                          FUNCTIONS                  
################################################################################

#           Proverka vvoda
def checking (var):
    try:
        var=int(var)
    except: TypeError
    return var

#           Cartoons
def cartoon():
    os.system('cls')
    pet.timer()
    happy = (pet.health+pet.joy+pet.fullness+pet.cleanliness-pet.thirst-pet.fatigue)//4
    if(happy>=85):
        print(pics[0])
    elif(happy>=35):
        print(pics[1])
    else:
        print(pics[2])
    pet.status()

#           Proverka otveta da-net
def yes_no(answer):
    positiv_answer = ['Yes', 'yes', 'Y','y','YES','д','да','Д','Да','ДА','!','у','У','е','ес','Е','Ес','Ессс','ессс','+', 'Угу','Ага',
                      'Конечно','конечно','I do','Почему бы и да',':)',')',')))','Eah', 'E', 'Yap', 'угу', 'ага', 'Да!', '!!!', '--', 'ляляля',
                      'Ляляля', 'start', 'давай', 'Давай', 'd', 'da', 'D', 'Da', 'DA', 'Start', 'Вперёд', 'Вперед','вперед','вперёд','го',
                      'ГОУ','Гоу','гоу','Го','ГО', 'go', 'Go', 'GO', 'I do!', '1']
    negativ_answer = ['No', 'no', 'N','n','NO','nea','Nea','net','NET', '-', ':(', ':(((', '(', ':C', 'stop', 'Stop', 'STOP', 'I do not',
                      'н', 'не', 'нет', 'Н', 'Не', 'Нет', 'НЕ', 'НЕТ', 'неа', 'неть', 'не хочу', 'надоело', 'скучно', 'хватит', 'ненене',
                      'не-не-не', 'нет-нет', 'не-не', '0', 'нетушки', 'бебебе', 'бе-бе-бе', 'ни в коем случае', 'фууу', 'пффф', 'стоп', 'харе',
                      'Неа', 'Неть', 'Не хочу', 'Надоело', 'Скучно', 'Хватит', 'Ненене', 'Не-не-не', 'Нет-нет', 'Не-не', 'Нетушки', 'Бебебе',
                      'Бе-бе-бе', 'Ни в коем случае', 'Фууу', 'Пффф', 'Стоп', 'Харе']
    while(True):
        if(answer in positiv_answer): return 1
        elif(answer in negativ_answer): return 0
        else:
            answer = input('Sorry, I don\'t understand. What would be your answer again?(Yes/No) ')


################################################################################
#                                          MAIN                  
################################################################################

############ SPISKI
game_ball = ['play with the ball', 'Play with the ball', 'ball', 'Ball']
game_guess = ['play guess number', 'Play guess number', 'guess number', 'Guess number']
clean_comb = ['comb fur','Comb fur','fur','Fur','comb','Comb']
clean_wash = ['wash','Wash','wash pet','wash pet','','']
clean_cut = ['cut','Cut','cut claws','Cut claws','claws','Claws']
heal_med = ['give medicine','Give medicine','medicine','Medicine','meds','Meds']
heal_inject = ['give injection','Give injection','injection','Injection','inject','Inject']
heal_treat = ['hug and treat','Hug and treat','hug','Hug','treat','Treat']
heal_vet = ['take to veterinary','Take to veterinary','vet','Vet','veterenary','Veterenary']

#### CIKL MENU (dva varianta vyhoda (zavesti pitomca i vyjti iz ))
while(True):
    os.system('cls')
    print("""Hello!
This is tamagochi game.

Enter 'start' to choose your pet
Enter 'rules' to read rules
Enter 'exit' to exit the game

""")
    menu = input("Enter  ")
    if(menu == 'start'):
        while(True):
            os.system('cls')
            user_pet = input("Choose your pet wisely:\n1. Dog\n"+dog[0]+"\n2. Cat\n"+cat[0]+"\n\nYou choose ")
            if(user_pet == 'cat' or user_pet == 'Cat'):
                while(True):
                    name = input("Enter name of your cat ")
                    if(yes_no(input("You want to name your cat "+name+", correctly? (Yes/No) "))):
                        pics = cat
                        pet = Cat(name)
                        break
                    else:
                        print("\nTry again.\n\n")
                        os.system('pause')
                        continue
                print("\nYour new pet is "+str(pet)+"\n")
                os.system('pause')
                break
            elif(user_pet == 'dog' or user_pet == 'Dog'):
                while(True):
                    name = input("Enter name of your dog ")        
                    if(yes_no(input("You want to name your dog "+name+", correctly? (Yes/No) "))):
                        pics = dog
                        pet = Dog(name)
                        break
                    else:
                            print("\nTry again.\n\n")
                            os.system('pause')
                            continue
                print("\nYour new pet is "+str(pet)+"\n")
                os.system('pause')
                break
            else:
                print("\nTry again.\n\n")
                os.system('pause')
                continue
    elif(menu == 'rules'):
        os.system('cls')
        print("""

You can choose your own pet, but remember that you will need
to care about it or it will die. Your pet has few characteristics:
 - 'health' - indicates level of health of your pet, you can heal it, if it
 will be ill.
 - 'fullness' - shows you does it want to eat, you will need to feed it.
 - 'thirst' - indecates how much your pet want to drink something.
 - 'fatigue' - shows you how tired is your pet, sometimes it need to rest.
 - 'cleanliness' - indicates how clear is your pet, maybe you need to clean it.
 - 'joy' - shows how cheerful is your pet, you can play with it.
'health', 'fullness', 'cleanliness' and 'joy' has the maximum index 100%
 which means, that your pet feels good, and if the index is close or equal to
 zero, that means your pet is in dangerous, if its health will be equal to
 zero your pet will die, and you won't be able to heal it.
On the contrary if 'thirst' or 'fatigue' will reach 100%, that means your pet
need some water or is tired and want to sleep.

""")
        os.system('pause')
        continue
    elif(menu == 'exit'):
        os.system('cls')
        print("\nBye bye!")
        os.system('pause')
        break
    else:
        print("\nYou entered something wrong, try again\n\n")
        os.system('pause')        
        continue
    
   
    ####                       GAME                              ####
    
    while(pet.health>0):
        cartoon()
        user_do = input('\nWhat do you want to do whith your pet?\n- feed\n- give drink\n- play\n- clean\n- let sleep\n- heal\n\nYou choose ')
#### KORMIT'        
        if(user_do in do_feed): 
            while(True):
                cartoon()
                if(pet.fullness == 100):
                    print(pet.name+' isn\'t hungry.\n')
                    os.system('pause')
                    break
                else:                
                    food = input('\nWhat type of food, do you want to give to '+pet.name+'? There are:\nfish, beef, chicken, soup, carrot, sausage, cream, cheese, pork,\ngreen, egg, sweet, nuts, apple, berries, grass, grits, liver,\nchips, preserves, jam, puree, noodles, bacon.\n\nYou choose ')
                    if(food in callories):
                        pet.feed(food)
                        if(yes_no(input('Do you want to give '+pet.name+' some more? (Yes/No) '))): continue
                        else: break
                    else:
                        print('\nThere is no such food...\n')
                        os.system('pause')
                        
#### POIT'                        
        elif(user_do in do_drink): 
            while(True):
                cartoon()
                if(pet.thirst == 0):
                    print(pet.name+' isn\'t thirsty.\n')
                    os.system('pause')
                    break
                else:                 
                    drink = input('\nWhat type of drink, do you want to give to '+pet.name+'? There are:\nwater, milk, juice, kefir, honey, soda.\n\nYou choose ')
                    if(drink in drinks):
                        pet.drinking(drink)
                        if(yes_no(input('Do you want to give '+pet.name+' some more? (Yes/No) '))): continue
                        else: break
                    else:
                        print('\nThere is no such drink...\n')
                        os.system('pause')
#### IGRAT'                        
        elif(user_do in do_play): 
            while(True):
                cartoon()
                if(pet.joy == 100):
                    print(pet.name+' doesn\'t want to play.\n')
                    os.system('pause')
                    break
                else:                
                    user_game = input('\nWhat type of game, do you want to play with '+pet.name+'? You can:\n- walk\n- play with the ball\n- play guess number\n\nYou choose ')
                    if(user_game == 'walk' or user_game == 'Walk'):
                        pet.joy(1,0)
                        if(yes_no(input('Do you want to play with '+pet.name+' something else? (Yes/No) '))): continue
                        else: break
                    elif (user_game in game_ball):
                        pet.joy(1,1)
                        if(yes_no(input('Do you want to play with '+pet.name+' something else? (Yes/No) '))): continue
                        else: break
                    elif (user_game in game_guess):
                        os.system('cls')
                        print('Welcome! This is...\n')
                        win = 0
                        game = 0
                        while(True):
                            print('GUESS THE NUMBER GAME!!!')
                            game += 1
                            u_try = 0
                            print('Range from 1 to 10')
                            num = randrange(1,11)
                            print('Number chosen...\n')
                            guess = checking(input('\nThe number is '))
                            while (guess!=num): 
                                u_try+=1
                                if (guess>10 or guess<1):
                                    print('\nNumber is out of range.')
                                elif(guess>num):
                                    print('\nNumber is less then guess.')
                                elif(guess<num):
                                    print('\nNumber is bigger then guess.')
                                elif(guess == num):
                                    print('\nYou guessed!')
                                    break
                                guess = checking(input('\nThe number is '))
                            if(u_try<2):    
                                win+=1
                            if(yes_no(input('Do you want to play again? (Yes/No) '))):
                                os.system('cls')
                                continue
                            else: break
                        pet.joy(game,win)    
                        if(yes_no(input('Do you want to play with '+pet.name+' something else? (Yes/No) '))): continue
                        else: break
                    else:
                        print('\nThere is no such game...\n')
                        os.system('pause')
#### MYT'                        
        elif(user_do in do_clean): 
            while(True):
                cartoon()
                if(pet.cleanliness == 100):
                    print(pet.name+' is clean\n')
                    os.system('pause')
                    break
                else:#               
                    u_clean = input('\nWhat type of cleaning would you choose? You can:\n-comb fur\n- wash pet\n- cut claws\n\nYou choose ')
                    if(u_clean in clean_comb):
                        pet.clean(15)
                        if(yes_no(input('Do you want to do something else to clean '+pet.name+'? (Yes/No) '))): continue
                        else: break
                    elif(u_clean in clean_wash):
                        pet.clean(25)
                        if(yes_no(input('Do you want to do something else to clean '+pet.name+'? (Yes/No) '))): continue
                        else: break
                    elif(u_clean in clean_cut):
                        pet.clean(10)
                        if(yes_no(input('Do you want to do something else to clean '+pet.name+'? (Yes/No) '))): continue
                        else: break
                    else:
                        print('\nThere is no such action...\n')
                        os.system('pause')

#### SPAT'                        
        elif(user_do in do_sleep): 
            while(True):
                cartoon()
                if(pet.fatigue == 0):
                    print(pet.name+' isn\'t tired.\n')
                    os.system('pause')
                    break
                else: #               
                    hours = checking(input('\nHow long do you want '+pet.name+' to sleep?\n\nYou choose (in hours amount)'))
                    if (hours>10):
                        print(pet.name+' can\'t sleep that long.')
                        continue
                    elif(hours>0):
                        os.system('cls')
                        print(pet[3])
                        pet.sleep(hours)
                        time.sleep(hours)
                        if(yes_no(input('Do you want to give '+pet.name+' more rest? (Yes/No) '))): continue
                        else: break
                    else:
                        print("\nYou entered something wrong, try again.\n")
                        os.system('pause')
                        
#### LECHIT'                        
        elif(user_do in do_heal): 
            while(True):
                cartoon()
                if(pet.health == 100):
                    print(pet.name+' doesn\'t need healing.\n')
                    os.system('pause')
                    break
                else:#                
                    u_heal = input('\nWhat type of healing would you choose? You can:\n- give medicine\n- give injection\n- hug and treat\n- take to veterinary\n\nYou choose ')
                    if(u_heal in heal_med):
                        pet.clean(15)
                        if(yes_no(input('Do you want to do something else to treat '+pet.name+'? (Yes/No) '))): continue
                        else: break
                    elif(u_heal in heal_inject):
                        pet.clean(25)
                        if(yes_no(input('Do you want to do something else to treat '+pet.name+'? (Yes/No) '))): continue
                        else: break
                    elif(u_heal in heal_treat):
                        pet.clean(10)
                        if(yes_no(input('Do you want to do something else to treat '+pet.name+'? (Yes/No) '))): continue
                        else: break 
                    elif(u_heal in heal_vet):
                        pet.clean(10)
                        if(yes_no(input('Do you want to do something else to treat '+pet.name+'? (Yes/No) '))): continue
                        else: break    
                    else:
                        print('\nThere is no such action...\n')
                        os.system('pause')
                        
#### EXIT                        
        elif(user_do == 'exit'):
            os.system('cls')
            if(yes_no(input('You want to leave '+pet.name+'?'))):
                print(pet.name+' will miss you!\n Bye-bye!')
                os.system('pause')
                break
            else:
                print('Let\'s get back to '+pet.name+'!\n')
                os.system('pause')
                
#### Oshibka vvoda                
        else:
            print('\nSorry, I don\'t understand, what do you want to do, please try again.\n')
            os.system('pause')
            
        #
    os.system('cls')
    print('''
    ___     ___
   /\ /\   /\ /\
  (  X  ) (  X  )
   \/_\/   \/_\/
     _________
    /_|_|_|_|_\
    \_|_|_|_|_/
     
''')
    print("Health of your pet is too low.\nBye-bye!\n\n")
    os.system('pause')
