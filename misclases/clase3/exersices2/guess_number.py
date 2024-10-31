import random

number_guess = random.randint(1,10)
guess = False

while not guess:
    number = int(input("Enter a number\n"))
    if number > number_guess:
        print("Your number is higher")
    elif number < number_guess:
        print("Your number is lower")
    else:
        print(f"You gussed the number is {number_guess}")
        guess = True