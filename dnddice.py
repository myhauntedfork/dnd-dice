import random
import time

def roll_dice(num):
    return random.randint(1, num)

def dice_number(dice):
        time.sleep(0.5)
        print('')
        print(f'Your roll is... {roll_dice(dice)}!')
        print('')
        time.sleep(0.5)


def dice_select():
    print("Please select one of the following dice to roll:")
    print('')
    time.sleep(1)
    print('[1] - D4')
    time.sleep(0.1)
    print('[2] - D6')
    time.sleep(0.1)
    print('[3] - D8')
    time.sleep(0.1)
    print('[4] - D10')
    time.sleep(0.1)
    print('[5] - D12')
    time.sleep(0.1)
    print('[6] - D20')
    time.sleep(0.1)
    print('')
    print('[7] - Quit')
    time.sleep(1)
    print('')
    print('Which dice would you like to roll?')
    choose_dice = input('>> ').strip().lower()

    if choose_dice in ('1', 'd4', '4'):
        dice_number(4)
    elif choose_dice in ('2', 'd6', '6'):
        dice_number(6)
    elif choose_dice in ('3', 'd8', '8'):
        dice_number(8)
    elif choose_dice in ('4', 'd10', '10'):   
        dice_number(10)
    elif choose_dice in ('5', 'd12', '12'):
        dice_number(12)
    elif choose_dice in ('6', 'd20', '20'):
        dice_number(20)
    elif choose_dice in ('7', 'quit'):
        return game_active == False
    else:
        print(f'"{choose_dice}" is not a valid choice.')
        return game_active == True

    return game_active == True

if __name__ == "__main__":
    game_active = True
    while game_active:
        game_active = dice_select()
