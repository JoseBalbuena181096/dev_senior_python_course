import asyncio

async def repet():
    for i in range(100000):
        print(i)
        if i % 1000 == 0:
            await asyncio.sleep(0)  # Cede el control al event loop


async def saludar():
    print("Hola")
    await asyncio.sleep(10)  # Espera 1 segundo sin bloquear
    await repet()
    print("Mundo")

# Para ejecutar una función asíncrona:
asyncio.run(saludar())

