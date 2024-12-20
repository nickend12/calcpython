import tkinter as tk
from tkinter import messagebox

# Función para realizar las operaciones
def click_boton(valor):
    entrada_texto.insert(tk.END, valor)

def borrar():
    entrada_texto.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada_texto.get())
        entrada_texto.delete(0, tk.END)
        entrada_texto.insert(tk.END, str(resultado))
    except:
        messagebox.showerror("Error", "Entrada no válida")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Elegante")
ventana.config(bg="#2E3B4E")  # Color de fondo elegante

# Configuración de la entrada de texto
entrada_texto = tk.Entry(ventana, font=("Arial", 18), width=15, borderwidth=2, relief="solid", justify="right")
entrada_texto.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones de la calculadora
botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
]

# Crear los botones y agregarlos a la ventana
for (texto, fila, col) in botones:
    if texto == "=":
        boton = tk.Button(ventana, text=texto, font=("Arial", 18), width=5, height=2, bg="#4CAF50", fg="white", command=calcular)
    else:
        boton = tk.Button(ventana, text=texto, font=("Arial", 18), width=5, height=2, bg="#f0f0f0", command=lambda valor=texto: click_boton(valor))
    boton.grid(row=fila, column=col, padx=5, pady=5)

# Botón para borrar
boton_borrar = tk.Button(ventana, text="C", font=("Arial", 18), width=5, height=2, bg="#F44336", fg="white", command=borrar)
boton_borrar.grid(row=5, column=0, padx=5, pady=5)

# Ejecutar la interfaz gráfica
ventana.mainloop()
