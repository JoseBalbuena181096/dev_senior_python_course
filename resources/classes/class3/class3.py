age = 14
country = 'GER'
userHasDNI = True

# First condition of the code
if age >= 21:
    print('You can buy alcohol in USA')
# if the  first condition is not true, the second condition will be executed
elif age >= 18:
    print('You can buy alcohol in COL')
# if the  previous condition is not true, the next condition will be executed, you can have as many elif as you want
elif age >= 16:
    print('You can buy alcohol in GER')
# if all the previous conditions are not true, the last condition will be executed
else:
    print('You can\'t buy alcohol')

# if condition:
#     actions
if age >= 21 and country == "USA":
    print('You can buy alcohol in USA')
elif age >= 18 and country == "COL":
    print('You can buy alcohol in COL')
elif age >= 16 and country == "GER":
    print('You can buy alcohol in GER')
else:
    # userHasDNI = False
    print('You can\'t buy alcohol')

# for variable in objectToIterate:
#     actions
# For each value of the i in the range of 10 (0-9)
# student = 0
# print(student)
# student = 1
# print(student)
# student = 2
# print(student)
# ...
# student = 9
# print(student)
for student in range(2):
    print(student)

# while condition:
#     actions

studentNumber = 0
while userHasDNI:
    studentNumber += 1
    print(studentNumber)
    if studentNumber == 10:
        userHasDNI = False

    if age >= 21 and country == "USA":
        print('You can buy alcohol in USA')
    elif age >= 18 and country == "COL":
        print('You can buy alcohol in COL')
    elif age >= 16 and country == "GER":
        print('You can buy alcohol in GER')
    else:
        userHasDNI = False
        print('You can\'t buy alcohol')
        
while userHasDNI:
    # block 1
    print("HELLO 1")
    
    # block 2
    if age >= 21 and country == "USA":
        print('You can buy alcohol in USA')
        # stop the block
        break
    elif age >= 18 and country == "COL":
        print('You can buy alcohol in COL')
    elif age >= 16 and country == "GER":
        print('You can buy alcohol in GER')
    else:
        userHasDNI = False
        print('You can\'t buy alcohol')

    #block 3
    print("HELLO 2")

print("############## WHILE ##############")

userHasDNI = True
while userHasDNI:
    
    age = int(input('Enter your age: '))
    country = input('Enter your country: ')
    
    # block 1
    if age >= 21 and country == "USA":
        print('You can buy alcohol in USA')
    elif age >= 18 and country == "COL":
        print('You can buy alcohol in COL')
    elif age >= 16 and country == "GER":
        print('You can buy alcohol in GER')
    else:
        userHasDNI = False
        print('You can\'t buy alcohol')

print("############## FOR ##############")

for student in range(1):
    age = int(input('Enter your age: '))
    country = input('Enter your country: ')
    
    # block 1
    if age >= 21 and country == "USA":
        print('You can buy alcohol in USA')
    elif age >= 18 and country == "COL":
        print('You can buy alcohol in COL')
    elif age >= 16 and country == "GER":
        print('You can buy alcohol in GER')
    else:
        userHasDNI = False
        print('You can\'t buy alcohol')

print("############## WHILE 100 STUDENTS  NO DNI ##############")

studentsWithoutDNI = 0
while studentsWithoutDNI <= 3:
    
    age = int(input('Enter your age: '))
    country = input('Enter your country: ')
    
    # block 1
    if age >= 21 and country == "USA":
        print('You can buy alcohol in USA')
    elif age >= 18 and country == "COL":
        print('You can buy alcohol in COL')
    elif age >= 16 and country == "GER":
        print('You can buy alcohol in GER')
    else:
        # studentsWithoutDNI = studentsWithoutDNI + 1;
        studentsWithoutDNI += 1 
        print('You can\'t buy alcohol')

print("############## FOR 10000 STUDENTS  JUST FIND 3 NO DNI ##############")

studentsWithoutDNI = 0
for student in range(10000):

    if studentsWithoutDNI == 3:
        break

    # block 0
    age = int(input('Enter your age: '))
    country = input('Enter your country: ')
    
    # block 1
    if age >= 21 and country == "USA":
        print('You can buy alcohol in USA')
    elif age >= 18 and country == "COL":
        print('You can buy alcohol in COL')
    elif age >= 16 and country == "GER":
        print('You can buy alcohol in GER')
    else:
        studentsWithoutDNI += 1 
        print('You can\'t buy alcohol')

studentsWithoutDNI = 0
for student in range(100):

    age = int(input('Enter your age: '))
    country = input('Enter your country: ')
    
    if country == "USA":
        print('You are not from COL, please come next student')
        continue

    if age <= 15:
        print('You can\'t buy alcohol')
        print('You are still in secondary you cant register to the university')
        continue
    
    hasDegree = False
    if age >= 18 and country == "COL" and hasDegree:
        print("Assigned a DNI")
        print("You can buy alcohol in COL")
        print("You are in the university")
        break

    
    


    