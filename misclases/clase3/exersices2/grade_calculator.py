# grade calculator
grade = float(input("Enter your grade\n"))
while ( grade > 100 or grade < 0):
    grade = float(input("Enter your grade\n"))

if grade >= 60:
    print("The student passed")
else:
    print("The student not passed")
