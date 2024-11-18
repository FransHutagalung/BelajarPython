class Animal :
    name = ''
    a = 0

    def __init__(self , name , a ):
        self.name = name
        self.a = a

    def _showValue(self , newValue):
         self.a += newValue


score = 10.3
gpa = "3.2"
is_student = False
score_string = str(score)
gpa_float = float(gpa)
int_score = int(score)

score_string += "1"

if __name__ == '__main__':

    print(f"type of socre is {type(score)}")
    print(int_score)
    print(f"score string is {score_string}")

    print(f"the score is {score}")
    animal = Animal(name='Lion' , a=20)
    print(f"animal name {animal.name}")
    if animal.a <= 0 :
        print('the animal a value is to shorter' , animal.a)
    else :
        print('the animal a value is normal', animal.a)


