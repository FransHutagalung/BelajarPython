import random
def one() :
    card = [
        'ace' , 
        '2' , 
        '3' , 
        '4' , 
        '5' , 
        '6' , 
        '7' , 
        '8' , 
        '9' , 
        '10' , 
        'jack' , 
        'queen' , 
        'king'
    ]

    print(f'before shuffle {card}')
    card2 = random.shuffle(card) # tidak mengembalikan nilai ini salah
    print(f'after shuffle {card}')

def two() :
    lowest_number = 1 
    highest_number = 100
    is_running = True 
    guesess = 0 

    secret_number = random.randint(lowest_number , highest_number)
    
    while is_running :
        guesess = input('guess a number => ')

        if guesess.isdigit() :
            pass
            guesess = int(guesess)
            if guesess < lowest_number and guesess > highest_number :
                print('u are out of range')
            elif guesess == secret_number :
                print('you win')
                break
            else :
                if guesess > secret_number :
                    print('too high')
                else :
                    print('too low')
                continue
        
        else :
            print('invalid guess ')
            print(f'select number between {lowest_number} and {highest_number}')
  
two()