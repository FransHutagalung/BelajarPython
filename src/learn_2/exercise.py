def calculator(operator , a , b) :
    if(operator == '+') :
        return a + b 
    elif(operator == '-') :
        return a - b
    elif(operator == '*') :
        return a * b
    elif(operator == '/') :
        return a / b
    else :
        return 'operator not found'
    
a = float(input('enter first number => '))
b = float(input('enter second number => '))
operator = input('enter operator => ')
result = calculator(operator , a , b)
print(f"result is {result.__round__(0)}")