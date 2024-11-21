def one() : 
    name = input('enter your name => ')

    while len(name) < 12 :
        name = input('enter your name => ') 
    
    print(f'your name is {name}')

def two():
    print(f'type q or quit to leave')
    name = input('enter your name => ')
    if not name == 'q' and name != 'quit' :
        while len(name) < 12 :
            name = input('enter your name => ') 
         
    print(f'your name is {name}')
    print('success')
    
two()
