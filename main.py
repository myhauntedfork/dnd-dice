import random
import time

def continue_():
    input("\npress enter to continue...\n")

def dice_number(dice):
        time.sleep(0.5)
        print('')
        print(f'Your roll is... {random.randint(1, dice)}!')
        print('')
        time.sleep(0.5)

def select_dice():
    
    dice = [
        'D4',
        'D6',
        'D8',
        'D10',
        'D12',
        'D20'
    ]

    dice_options = {
        '1': 4, 'd4': 4,
        '2': 6, 'd6': 6,
        '3': 8, 'd8': 8,
        '4': 10, 'd10': 10,
        '5': 12, 'd12': 12,
        '6': 20, 'd20': 20,
        '7': 'quit', 'quit': 'quit'
    }

    print("Select one of the following dice to roll:\n")
    for i, die in enumerate(dice, start=1):
        print(f'[{i}] - {die}')
    print("[7] - quit")

    choose_dice = input('\nWhich dice would you like to roll?\n>> ')
    answer = choose_dice.lower().strip()

    if answer in dice_options:
        if dice_options[answer] == 'quit':
             return False
        dice_number(dice_options[answer])
        continue_()
        return True
    else:
        print(f'{choose_dice} is not a valid die.')

if __name__ == '__main__':
     game_active = True
     while game_active:
          game_active = select_dice()