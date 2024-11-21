final_amount = 0 
principal_balance = 0 
interest_rate = 0 
time_periods = 0 

while principal_balance <= 0 :
    principal_balance = float(input('enter a principal balance => '))
    if principal_balance <  0 :
        print('principal can not less than or equal 0') 
        
while interest_rate <= 0 :
    interest_rate = float(input('enter a interest rate  => '))
    if interest_rate <  0 :
        print('interest rate  can not less than or equal 0') 
        
while time_periods <= 0 :
    time_periods = float(input('enter a time periods => '))
    if time_periods <  0 :
        print('time periods can not less than or equal 0') 
        
final_amount = np.fv(interest_rate , time_periods , principal_balance)