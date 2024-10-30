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

# Boolean variable to control the loop based on whether the user has a DNI
userHasDNI = True
while userHasDNI:
    # Prompt the user to input their age and country
    age = int(input('Enter your age: '))
    country = input('Enter your country: ')
    
    # block 1: Conditions to determine if the user can legally buy alcohol
    if age >= 21 and country == "USA":
        print('You can buy alcohol in USA')
    elif age >= 18 and country == "COL":
        print('You can buy alcohol in COL')
    elif age >= 16 and country == "GER":
        print('You can buy alcohol in GER')
    else:
        # If none of the above conditions are met, the loop stops
        userHasDNI = False
        print('You can\'t buy alcohol')

print("############## FOR ##############")

# Single iteration with a for loop
for student in range(1):
    age = int(input('Enter your age: '))
    country = input('Enter your country: ')
    
    # block 1: Same alcohol eligibility conditions as above
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

# Initialize counter for students without a DNI
studentsWithoutDNI = 0
while studentsWithoutDNI <= 3:
    age = int(input('Enter your age: '))
    country = input('Enter your country: ')
    
    # block 1: Check alcohol eligibility conditions
    if age >= 21 and country == "USA":
        print('You can buy alcohol in USA')
    elif age >= 18 and country == "COL":
        print('You can buy alcohol in COL')
    elif age >= 16 and country == "GER":
        print('You can buy alcohol in GER')
    else:
        # If the user can't buy alcohol, increment the counter for students without DNI
        studentsWithoutDNI += 1 
        print('You can\'t buy alcohol')

print("############## FOR 10000 STUDENTS  JUST FIND 3 NO DNI ##############")

# Reset counter for students without DNI
studentsWithoutDNI = 0
for student in range(10000):  # Iterate over a large range

    # If we have found 3 students without DNI, break out of the loop
    if studentsWithoutDNI == 3:
        break

    # block 0: User inputs age and country again
    age = int(input('Enter your age: '))
    country = input('Enter your country: ')
    
    # block 1: Same alcohol eligibility checks
    if age >= 21 and country == "USA":
        print('You can buy alcohol in USA')
    elif age >= 18 and country == "COL":
        print('You can buy alcohol in COL')
    elif age >= 16 and country == "GER":
        print('You can buy alcohol in GER')
    else:
        # Increment counter if student can't buy alcohol
        studentsWithoutDNI += 1 
        print('You can\'t buy alcohol')

# Another for loop to iterate over 100 students
studentsWithoutDNI = 0
for student in range(100):

    # Input age and country for each student
    age = int(input('Enter your age: '))
    country = input('Enter your country: ')
    
    # Check if the country is "USA"
    if country == "USA":
        print('You are not from COL, please come next student')
        continue  # Skip the rest of the loop for this iteration and move to the next student

    # Check if the age is 15 or below
    if age <= 15:
        print('You can\'t buy alcohol')
        print('You are still in secondary you cant register to the university')
        continue  # Skip to the next iteration if the student is in secondary

    # Condition for assigning a DNI and determining university eligibility
    hasDegree = False
    if age >= 18 and country == "COL" and hasDegree:
        print("Assigned a DNI")
        print("You can buy alcohol in COL")
        print("You are in the university")
        break  # Break the loop once a student meets all criteria and has been assigned a DNI


    
    


    