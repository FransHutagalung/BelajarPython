# status = bool(input('enter status => ')) # kalau begini jika dia input true maka dia bisa vote jika input kosong maka dia akan false

status = input('enter a status => ').strip().lower() == 'true'

age = int(input('enter age => '))

if status == True and age >= 15 :
    print('you can vote with your family')
elif status == True or age >= 20 :
    print('you can vote')
else :
    print('you cannot vote')