"""
v1 In new version updated player choice for restart game after it ended.
"""
from random import randrange

number = randrange(1, 100)
check = 0
player_choice = 0
player_repeat = 0

#print(number)
while True:
    player_choice = int(input('Enter your number: \n>>>'))
    check += 1
    if number == player_choice:
        print(str(number) + f' Yes you a right! You guessed the number for {check} tries!')
        print('Do you wanna play again? Yes or No')
        player_repeat = str(input('Enter your choice: \n>>>')).lower()
        if player_repeat == 'yes' or player_repeat == 'y':
            number = randrange(1, 100)
            check = 0
            continue
        elif player_repeat == 'no' or player_repeat == 'n':
            print('Have a nice day!')
            break
        else:
            print('Make your choice')
            player_repeat = str(input('Enter your choice: \n>>>')).lower()
            if not player_repeat == 'yes' or player_repeat == 'y':
                break
            else:
                number = randrange(1, 100)
                check = 0
                continue
    elif number > player_choice:
        print('Entered your number had less than guessed number.Try again')
        print('You have ' + str(check) + ' tries!')
        if check == 5:
            print('Do you wanna play again? Yes or No')
            player_repeat = str(input('Enter your choice: \n>>>')).lower()
            if player_repeat == 'yes' or player_repeat == 'y':
                number = randrange(1, 100)
                check = 0
                continue
            elif player_repeat == 'no' or player_repeat == 'n':
                print('Have a nice day!')
                break
            else:
                print('Make your choice')
                player_repeat = str(input('Enter your choice: \n>>>')).lower()
                if not player_repeat == 'yes' or player_repeat == 'y':
                    break
                else:
                    number = randrange(1, 100)
                    check = 0
                    continue
    else:
        print('Entered your number had greater than guessed number.Try again')
        print('You have ' + str(check) + ' tries!')
        if check == 5:
            print('Do you wanna play again? Yes or No')
            player_repeat = str(input('Enter your choice: \n>>>')).lower()
            if player_repeat == 'yes' or player_repeat == 'y':
                number = randrange(1, 100)
                check = 0
                continue
            elif player_repeat == 'no' or player_repeat == 'n':
                print('Have a nice day!')
                break
            else:
                print('Make your choice')
                player_repeat = str(input('Enter your choice: \n>>>')).lower()
                if not player_repeat == 'yes' or player_repeat == 'y':
                    break
                else:
                    number = randrange(1, 100)
                    check = 0
                    continue
