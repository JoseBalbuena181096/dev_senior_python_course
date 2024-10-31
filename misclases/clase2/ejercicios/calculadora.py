
def is_float(number):
    try:
        float(number)
        return True
    except ValueError:
        return False
    
number1 = input("Type the first number on the console \n")
number2 = input("Type the second number on the console \n")

if(is_float(number1) and is_float(number2)):
    number1 = float(number1)
    number2 = float(number2)

    add = number1 + number2
    substraction  = number1 - number2
    multiplication = number1 * number2
    division = number1 / number2

    print(f'The add of {number1} + {number2} = {add}')
    print(f'The substraction of {number1} - {number2} = {substraction}')
    print(f'The multiplication of {number1} + {number2} = {multiplication}')
    print(f'The division of {number1} + {number2} = {division}')


else:
    print("Error the data input is not a number")