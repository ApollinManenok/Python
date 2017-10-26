####   Tamagochi game

################################################################################
#                                          IMPORT                  
################################################################################


from random import *
from myobjectmodule import *


################################################################################
#                                          FUNCTIONS                  
################################################################################

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


################################################################################
#                                          MAIN                  
################################################################################

print("Hello!\n This is tamagochi game.\nChoose your critter ")
print('\n________________________________\n\n       |\\                                    /|\n       |  \\                                /  |\n       |    \\______________/    |\n       |                                       |\n       |       (_||_)        (_||_)        |\n       \\                                     /     \n        \\         >.:   T   :.<          /       \n          \\________________/           \n\n________________________________\n')


#print(Critter.health)
