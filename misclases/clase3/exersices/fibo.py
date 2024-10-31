
term = int(input("Type the number of terms of the fibo serie\n"))

a,b = 0, 1

for i in range(term):
    print(a, end=', ')
    tempA = a
    a = b
    b = tempA + b

    # a, b = 0, 1
    # for _ in range(n):
    #     a, b = b, a + b

    