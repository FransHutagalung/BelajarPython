food = []

vegetables = [
    'tomato' ,
    'carrot' , 
    'potato'
    ]

fruits = [
    'apple' ,
    'manggo' ,
    'grape' ,
    'banana'
] 

meal = [
    'rice' ,
    'noodles' ,
    'steak' ,
    'chicken'
]

food = [
    vegetables , 
    fruits , 
    meal
]

print(food[::])


for collection in food :
    for x in collection :
        print(x , end=' ')
    print('')