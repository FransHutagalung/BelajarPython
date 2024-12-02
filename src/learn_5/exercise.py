import time

def exercise1() :
    foods = []
    price = []
    qty = []
    total = 0 


    while True :
        food = input('enter a food to buy ( q to quit ) => ')
        if food == 'q' :
            break
        else : 
            foods.append(food)
            price.append(int(input(f'enter price of {food} => ')))



    print('\nyour foods list')
    for x in range (len(foods)) :
        print(f'{foods[x]:<12} => Rp.{price[x]} ') # akan menggeser food ke kiri sebanyak 12 space 


    print('\n')

    for x in range (len(foods)) :
        qty.append(int(input(f'enter the quantity of {foods[x]:<10} =>  :')))
        total += price[x] * qty[x]
        
    print('\n')
    print('your final bill is ')

    for x in range (len(foods)) :
        print(f'{foods[x]:<12} => Rp.{price[x] * qty[x]}')
        time.sleep(1)
        

    print(f'\ntotal => Rp.{total}')

def exercise2() :
    calculator_ui = [
        ['1' , '2' , '3'] , 
        ['4' , '5' , '6'] , 
        ['7' , '8' , '9'] , 
        ['*' , '0' , '#'] , 
    ]
    
    for cal in calculator_ui :
        for c in cal :
            print(f'{c:<3}' , end = ' ')
        print('\n')
        
def exercise3() :
    question = (
        'What is the next Capital City of Indonesia ? ' , 
        'When Indonesian people celebrate teachers day ? ' , 
        'When Indonesian people celebrate independence day ? ' ,
        'What is the symbol of Indonesia ? ' ,
        'Who is the Indonesia President ? ' ,
    )
    
    option = (
        ('Jakarta' , 'Nusantara' , 'Medan' , 'Jawa') ,
        ('25 November' , '1 January' , '10 February' , '17 Agustus') ,
        ('25 November' , '1 January' , '10 February' , '17 Agustus') ,
        ('Gambir' , 'Pancasila' , 'Bintang' , 'Merah - Putih') ,
        ('Prabowo' , 'Joko Widodo' , 'Bintang' , 'Jukal') ,
    )
    
    answer = (
        'b' , 
        'a' , 
        'd' , 
        'b' , 
        'a' ,
    )
    
    def checkAnswer() : 
        score = 0
        for q , a in zip(question , answer) :
            if userAnswer[question.index(q)] == str(a) :
                score += 1
        return score
    
    userAnswer = []
    
    n = 1 
    for q in question :
        print(f'{n}.{q}')
        for letter ,  o in zip('abcd' , option[n-1]) :
            print(f' {letter}.{o}')
        userAnswer.append(input('your answer => '))
        print('\n')
        n += 1
        
    print('\n')
    print(f'your score is {checkAnswer()}')
    
def exercise4() :
    menu = {
        'Nasi Goreng' : 14000 ,
        'Mie Goreng' : 15000 ,
        'Bakso' : 10000 ,
        'Es Teh' : 5000 ,
        'Es Jeruk' : 5000 ,
        'Nasi Padang' : 18000
    }
    
    total = 0 
    
    print('----------MENU--------------')
    for key , value in menu.items() :
        print(f'{key:<15} => Rp.{value}')
    print('----------------------------')
    
    while True :
        order = input('enter your order ( q to quit ): ')
        if(order == 'q') :
            break
        elif order in menu :
            total += menu[order]
            print(f'your order is {order} and price is Rp.{menu[order]}')
        else :
            print('your order is not in the menu')

    print(f'your total is {total}')

print('\n')
exercise4()