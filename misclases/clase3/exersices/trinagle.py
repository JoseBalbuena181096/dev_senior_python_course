from math import sqrt

first_leg = float(input("Enter the first leg "))
second_leg = float(input("Enter the second leg "))

hypotenuse = sqrt(first_leg**2 + second_leg**2)
print(f'The hipotenuse of {first_leg} and {second_leg} is {hypotenuse}')
