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
    while (True):
        u_try+=1
        if(guess == 0):
            print('\nStop the game.')
            break
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
