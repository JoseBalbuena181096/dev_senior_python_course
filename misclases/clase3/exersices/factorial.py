n = int(input("Type the number of factorial to calculate\n"))

fact = 1
for i in range(1, n):
    fact = (n-i) * fact
fact *= n

# fact = 1
# for i in range(2, n+1):
#     fact *= i 

print(fact)