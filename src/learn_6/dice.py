import random
# print('\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518')

def print_dice(number):
    dice_faces = {
        1: [
            "\u250C\u2500\u2500\u2500\u2500\u2500\u2510",
            "\u2502     \u2502",
            "\u2502  \u25CF  \u2502",
            "\u2502     \u2502",
            "\u2514\u2500\u2500\u2500\u2500\u2500\u2518"
        ],

        2: [
            "\u250C\u2500\u2500\u2500\u2500\u2500\u2510",
            "\u2502\u25CF    \u2502",
            "\u2502     \u2502",
            "\u2502    \u25CF\u2502",
            "\u2514\u2500\u2500\u2500\u2500\u2500\u2518"
        ],

        3: [
            "\u250C\u2500\u2500\u2500\u2500\u2500\u2510",
            "\u2502\u25CF    \u2502",
            "\u2502  \u25CF  \u2502",
            "\u2502    \u25CF\u2502",
            "\u2514\u2500\u2500\u2500\u2500\u2500\u2518"
        ],

        4: [
            "\u250C\u2500\u2500\u2500\u2500\u2500\u2510",
            "\u2502\u25CF   \u25CF\u2502",
            "\u2502     \u2502",
            "\u2502\u25CF   \u25CF\u2502",
            "\u2514\u2500\u2500\u2500\u2500\u2500\u2518"
        ],

        5: [
            "\u250C\u2500\u2500\u2500\u2500\u2500\u2510",
            "\u2502\u25CF   \u25CF\u2502",
            "\u2502  \u25CF  \u2502",
            "\u2502\u25CF   \u25CF\u2502",
            "\u2514\u2500\u2500\u2500\u2500\u2500\u2518"
        ],

        6: [
            "\u250C\u2500\u2500\u2500\u2500\u2500\u2510",
            "\u2502\u25CF   \u25CF\u2502",
            "\u2502\u25CF   \u25CF\u2502",
            "\u2502\u25CF   \u25CF\u2502",
            "\u2514\u2500\u2500\u2500\u2500\u2500\u2518"
        ],
    }

    for line in dice_faces[number]:
        print(line)
        
dice_faces = {
        1: [
            "\u250C\u2500\u2500\u2500\u2500\u2500\u2510",
            "\u2502     \u2502",
            "\u2502  \u25CF  \u2502",
            "\u2502     \u2502",
            "\u2514\u2500\u2500\u2500\u2500\u2500\u2518"
        ],

        2: [
            "\u250C\u2500\u2500\u2500\u2500\u2500\u2510",
            "\u2502\u25CF    \u2502",
            "\u2502     \u2502",
            "\u2502    \u25CF\u2502",
            "\u2514\u2500\u2500\u2500\u2500\u2500\u2518"
        ],

        3: [
            "\u250C\u2500\u2500\u2500\u2500\u2500\u2510",
            "\u2502\u25CF    \u2502",
            "\u2502  \u25CF  \u2502",
            "\u2502    \u25CF\u2502",
            "\u2514\u2500\u2500\u2500\u2500\u2500\u2518"
        ],

        4: [
            "\u250C\u2500\u2500\u2500\u2500\u2500\u2510",
            "\u2502\u25CF   \u25CF\u2502",
            "\u2502     \u2502",
            "\u2502\u25CF   \u25CF\u2502",
            "\u2514\u2500\u2500\u2500\u2500\u2500\u2518"
        ],

        5: [
            "\u250C\u2500\u2500\u2500\u2500\u2500\u2510",
            "\u2502\u25CF   \u25CF\u2502",
            "\u2502  \u25CF  \u2502",
            "\u2502\u25CF   \u25CF\u2502",
            "\u2514\u2500\u2500\u2500\u2500\u2500\u2518"
        ],

        6: [
            "\u250C\u2500\u2500\u2500\u2500\u2500\u2510",
            "\u2502\u25CF   \u25CF\u2502",
            "\u2502\u25CF   \u25CF\u2502",
            "\u2502\u25CF   \u25CF\u2502",
            "\u2514\u2500\u2500\u2500\u2500\u2500\u2518"
        ],
    }


def display_dice(dice):
    for row_index in range(5):
        for die_value in dice:
            print(dice_faces[die_value][row_index], end=' ')
        print()
    for x , num in zip(range(len(dice)) , dice) :
        # print(f'{num:^6}' , end=' ' if x == 0 else '{num:^8}' , end=' ' )
        print(f'{num:^7}' , end=' ')
        # if(x==0) :
        #     # print('pertama')
        #     print(f'{num:^7}' , end=' ')
        # else :
        #     if x != len(dice)-1 :
        #     else :
        #         print(f'{num:^7}' , end=' ')
        # print('|' , end=' ')
    print()
        
# print_dice(2)
print('wanna play a game')
dice = []

while True :
    user = input('enter your choice (y/n)=> ') 
    if user.lower() == 'n' :
        break 
    else :
        qty = input('how many dice do you want to roll => ')
        if qty.isdigit() :
            dice = []
            qty = int(qty)
            for x in range (qty) :
                user_choice = random.randint(1,6)
                # print_dice(user_choice)    
                dice.append(user_choice)
            # print(dice)
            display_dice(dice)
            print(f'total is {sum(dice)}')
            print('wanna play again ?')
        else :
            print('invalid input')
            


