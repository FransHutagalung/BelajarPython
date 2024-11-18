import math 

def exercise1() : 
    length = int(input('enter length of rectangle => '))
    width = int(input('enter width of rectangle => '))
    wide = length * width   
    print(f'area of rectangle is {wide}')
    
def exercise2() : 
    item = input('enter item name => ')
    quantity = int(input('enter quantity => '))
    price = float(input('enter price => '))
    total = quantity * price
    print(f"you buy {item}")
    print(f"totat price is ${total}")
    
def circumreference() :
    radius = float(input('enter radius =>> '))
    _circumreference =  2 * math.pi * radius
    print(f"circumreference is {_circumreference.__round__(2)}")

def circle_area() : 
    radius = float(input('enter radius =>> '))
    _area = math.pi * radius * radius
    print(f"area of circle is {_area.__round__(2)}")
    #round 2 agar hanya menampilkan 2 angka dibelakang koma 
    
def pythagoras () :
    a = float(input('enter a => '))
    b = float(input('enter b => '))
    _pythagoras = math.sqrt(pow(a,2) + pow(b,2))
    print(f"pythagoras is {_pythagoras.__round__(2)}")


pythagoras()

