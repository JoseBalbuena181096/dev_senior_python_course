import tkinter as tk

def convertir():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        resultado.config(text=f'Resultado fahrenheit {fahrenheit:.2f} °F')
    except:
        print('An exception ocurred')
        resultado.config(text="Ingrese un numero valido")

root = tk.Tk()
root.title("Conversor de Temperatura")
root.geometry("500x200")

# Widgets
tk.Label(root, text="Ingrese temperatura en °C: ").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text='Convertir', command=convertir).pack(pady=5)

resultado = tk.Label(root, text="")
resultado.pack(pady=5)

root.mainloop()



