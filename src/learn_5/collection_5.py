country = {
    'usa' : 'new york' , 
    'indonesia' : 'jakarta' ,
    'japan' : 'tokyo' ,
    'malaysia' : 'kuala lumpur'
}

if (country.get('usa')) : # mengecek apakah ada index indonesia 
    print('the capital exists')
    print(country['indonesia'])
else :
    print('the capital does not exist')
    
    
country.update({
    'germany' : 'berlin'
}) # menambah data  jika data nya belum ada sebelumnya

print(f'key , {country.keys()}')
print(f'value , {country.values()}')

print(country)

country.update({
    'usa' : 'washington'
})# mengedit data jika data nya sudah ada
print(country)


try :
    country.pop('malaysia') # menghapus data
except :
    print('key not found')
    
print(country)
country.popitem() # menghapus data terakhir
print(country) 


# country.clear() # menghapus semua data
# print(country)


item = country.items()
# print(item)

for x , value in country.items() :
    print(f'x => {x} , value => {value}')