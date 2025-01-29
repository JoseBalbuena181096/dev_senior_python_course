# Program to compare numbers
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
    if(number1 == number2):
        print(f'{number1} = {number2}')
    elif (number1 > number2):
        print(f'{number1} > {number2}')
    else:
        print(f'{number1} < {number2}')

else:
    print("Error the data input is not a number")