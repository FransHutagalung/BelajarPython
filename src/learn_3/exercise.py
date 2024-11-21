name = input('enter your name => ')

if len(name) < 12 :
    print('your name is too short')
elif name.find(' ') != -1 :
    print('name can not include a space')
elif not name.isalpha() :
    print('your name is invalid')
else :
    print(f'welcome {name}')