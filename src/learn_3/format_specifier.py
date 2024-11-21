price1 = 12423.14159
price2 = -3224.2121
price3 = 1122.34

print(f'price 1 is {price1:.2f}') # menampilkan 2 angka dibelakang koma
print(f'price 2 is {price2:.2f}') # menampilkan 2 angka dibelakang koma
print(f'price 3 is $ {price3:10}') # menampilkan 10 len jika tidak ada maka akan diisi space
print(len(str(price3)))


print(f'price 1 => $ {price1:010}') # menampilkan 10 angka jika tidak ada maka akan diisikan 0
print(f'price 2 => $ {price2:10.2f}') # menampilkan 10 angka jika tidak ada maka akan diisikan 0    

print('\n')

# angka sebelah kiri dan lebar string minimal 10
print(f'price 1 is => {price1:<10}') # menampilkan 10 len jika tidak ada maka akan diisi space
print(f'price 2 is => {price2:<10}') # menampilkan 10 len jika tidak ada maka akan diisi space
print(f'price 3 is => {price3:<10}') # menampilkan 10 len jika tidak ada maka akan diisi space

print('\n')

# angka sebelah kanan dan lebar string minimal 10
print(f'price 1 is => {price1:>10}') # menampilkan 10 len jika tidak ada maka akan diisi space
print(f'price 2 is => {price2:>10}') # menampilkan 10 len jika tidak ada maka akan diisi space
print(f'price 3 is => {price3:>10}') # menampilkan 10 len jika tidak ada maka akan diisi space

print('\n')

# angka sebelah tengah
print(f'price 1 is => {price1:^10}') # menampilkan 10 len jika tidak ada maka akan diisi space
print(f'price 2 is => {price2:^10}') # menampilkan 10 len jika tidak ada maka akan diisi space
print(f'price 3 is => {price3:^10}') # menampilkan 10 len jika tidak ada maka akan diisi space

print('\n')


print(f'price 1 is => {price1:-^10}') # menampilkan 10 len jika tidak ada maka akan diisi -
print(f'price 2 is => {price2:-^10}') # menampilkan 10 len jika tidak ada maka akan diisi -
print(f'price 3 is => {price3:*^10}') # menampilkan 10 len jika tidak ada maka akan diisi *


print('\n')


print(f'price 1 is => {price1: ,.2f}') 
print(f'price 2 is => {price2: ,}') 
print(f'price 3 is => {price3: ,}') 

