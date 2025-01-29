# Convert units

def is_float(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

length = input("Enter the length in meters\n")
if is_float(length):
    # convert the units
    meters = float(length)
    centimeters = meters * 100
    milimeters = centimeters * 10
    print(f'{meters} m is {centimeters} cm ')
    print(f'{meters} m is {milimeters} cm ')
else:
    print("The data enter is not a number ")