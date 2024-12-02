import random


# print(help(random))

num = random.randint(1,6)
print(num)

#random floating point number
ran = random.random()
print(ran)
user = None 

options = ['scissor' , 'rock' , 'paper']

computer = random.choice(options)

while True :
    user = input('enter your choice => ')
    if (user == 'scissor' and computer == 'paper') or (user == 'paper' and computer == 'rock') or (user == 'rock' and computer == 'scissor') :
        print('you win')
    elif user == computer :
        print('draw')
        continue
    else :
        print('you lose')
        break

print(f'computer choice is => {computer}')