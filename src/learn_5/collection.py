fruit = ['apple' , 'manggo' , 'grape' , 'banana' , 'watermelon' , 'strawberry'] # list 
print(fruit)
print(fruit[0]) # menampilkan index ke 5

mahasiswa = {
    'nama' : 'adhi hutagalung' ,
    'npm' : '222510097' ,
    'kelas' : '5 Ti Cerdas 2'
}

print(mahasiswa['npm'])


print(fruit[::2]) # index kelipatan 2
print(fruit[::-1]) #reversed
print(fruit[:])

fruit[0] = 'pineaple' 
fruit.append('kiwi') # menambahkan item ke dalam list

print(fruit[:])
print(fruit[1:3]) # dari index 1 sampai index 2 <3


animal : list[dict] = [
    {
    'name' : 'lion' ,
    'a' : 20} ,
    {
    'name' : 'tiger' ,
    'a' : 10} ,
    {
    'name' : 'elephant' ,
    'a' : 30} ,
    {
    'name' : 'monkey' ,
    'a' : 5
    }
    ]

for i in animal :
    print(f'animal name => {i['name']}')
    
# print(dir(animal))
# print(help(animal))


print("apple" in fruit)