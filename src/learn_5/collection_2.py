hobies = [
    'Drawing' ,
    'Fishing' ,
    'Reading' ,
    'Climbing'
]


anotherhobies = [
    'Cooking' , 
    'Desaining'
]

print(hobies[::])
hobies.remove('Fishing') # menghapus elemen dari list 
print(hobies[::])

print(hobies.index('Climbing')) # mencari index dari elemen dalam list
print(hobies[2])


print(hobies[::])
hobies.insert(2 , 'Dancing') # menambahkan elemen ke dalam list
print(hobies[::])


hobies.insert(-1 , 'swimming')
print(hobies[::])

hobies.insert(-2 , 'Gaming')
print(hobies[::])

# hobies.append(anotherhobies[::])
# print(hobies[::])


for x in anotherhobies : 
    hobies.append(x)


print(hobies[::])
hobies.extend(anotherhobies)


hobies.sort() # sorting array
print(hobies[::])

hobies.reverse() # reverse array
print(hobies[::])

hobies.clear() # clear array
print(hobies[::])

# print(hobies.index('smoking'))

hobies.count('smoking')