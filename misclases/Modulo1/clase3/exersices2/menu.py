# Greeting and farewell menu
goodbye = False

while not goodbye:
    name = input("Enter your name \n")
    select = int(input("1) greet\n2) say goodbye \n3) exit\n"))
    if select == 1:
        print(f'Hello {name}')
    elif select == 2:
        print(f'Goodbye {name}')
    elif select == 3:
        print("Finish program")
        goodbye = False
        break