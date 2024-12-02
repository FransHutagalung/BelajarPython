students = [
    'Fransiskus' , 
    'Hutagalung' ,
    'Adhi' ,
    'Marnaek'
]

try :
    print(students[4])
except IndexError :
    print('index not found')
    

nameToSearch = input('enter member name to search : ')

try :
    index = students.index(nameToSearch)
except :
    index = - 1;
    
if index == -1 :
    print(f'{nameToSearch} not found')
else :
    print(f'{nameToSearch} found at index {index}')