credit_number : str  = '123-456-898'

print(credit_number[0]) #0 index pertama
print(credit_number[2:4]) # 123- dari index 0 dan sampai index 3 parameter pertama asal , parameter kedua parameter akhir

# credit_number[2] = 'p'
print(credit_number[5:]) # dari index 5 sampai akhir
print(credit_number[:5]) # dari awal sampai index 4
print(credit_number[-1]) # index terakhir

print(credit_number[::2]) # index 0,2,4,6,8 =>  index kelipatan 2 => 134688
print(credit_number[::3]) # index 0,3,6, =>  index kelipatan 3

print(f"credit number last 4 digit character is {credit_number[-4:]}")

reverse_credit_number = credit_number[::-1] # reverse string
print(reverse_credit_number)


print(help(str))