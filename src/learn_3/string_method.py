from encodings.aliases import aliases

nama : str = 'adhi  marnaek     fransiskus      Hutagalung'
phone_number : str = '0812-3456-7890'

#capitalize 
print(nama.capitalize()) #tugasnya adalah membuat huruf pertana menjadi huruf kapital 

#casefold
print(nama.casefold()) #tugasnya adalah membuat semua huruf menjadi huruf kecil

#center
print(nama.center(50)) #tugasnya adalah membuat string menjadi center
# semisal kita buat width nya adalah 50 maka nanti akan ada str dengan width 50 namun str sebelumnya akan berada di tengah diantara space

#count
print(f"total huruf a adalah {nama.count('a')}") #tugasnya adalah menghitung jumlah huruf a di dalam string


# print(f'encoding yang tersedia adalah {aliases}')

#encoded
print(nama.encode(encoding='utf32' , errors='ignore')) #tugasnya adalah membuat string menjadi encoded

#endswith
print(nama.endswith('a')) #tugasnya adalah mengecek apakah string tersebut akhir dengan huruf 'a'

#expandtabs()
print(nama.expandtabs(5)) #tugasnya adalah membuat tab menjadi spasi


#find 
print(nama.find('Huta')) #tugasnya adalah untuk mencari spesifik key pada str return index 

#format
print(nama.format('hutagalung')) #tugasnya adalah memformat string di dalam str

print(nama.upper()) #tugasnya adalah membuat semua huruf menjadi huruf besar


print(phone_number.replace('-' , ' ')) # tugasnya adalah mengganti - menjadi spaso  di dalam string
