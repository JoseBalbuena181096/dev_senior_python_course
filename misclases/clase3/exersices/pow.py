# pow 
base = int(input("Introduce the base "))
exp = int(input("Introduce the exponete "))

result = 1
for i in range(exp):
    result *= base
print(result)