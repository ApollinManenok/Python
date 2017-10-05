from random import *

print ('21 game')
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
