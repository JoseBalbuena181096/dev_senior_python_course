def is_float(number):
    try:
        float(number)
        return True
    except ValueError:
        return False
    
age = input("Type your age \n")
if is_float(age):
    age = float(age)
    if age >= 18:
        print("Your age is equal or greater than 18, you can vote")
    else:
        print("Your age is less than 18, you can't vote")
else:
    print("Error type a number please ")