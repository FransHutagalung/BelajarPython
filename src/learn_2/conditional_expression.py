import datetime

x = datetime.datetime.now().year
print(x)

num = 5 
year_of_entry = 2023



print(num if num > 0 else 'nothing to see')
print('Positife' if num > 0 else 'Negative')


status = "mahasiswa baru" if year_of_entry == x else f"bukan mahasiswa baru telah {x - year_of_entry} tahun  belajar "

print(status)