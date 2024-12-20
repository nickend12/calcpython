import tkinter as tk
from tkinter import messagebox
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

# Función para calcular el área, perímetro y altura del trapecio
def calcular():
    try:
        base_mayor = float(entry_base_mayor.get())  # type: ignore
        base_menor = float(entry_base_menor.get())
        lado3 = float(entry_lado3.get())
        lado4 = float(entry_lado4.get())

        if lado3 != lado4:
            messagebox.showerror("Error", "El trapecio no es isósceles. La altura no se puede calcular automáticamente.")
            return

        # Calcular altura
        semi_base = (base_mayor - base_menor) / 2
        altura = sqrt(lado3 ** 2 - semi_base ** 2)

        # Calcular perímetro
        perimetro = base_mayor + base_menor + lado3 + lado4

        # Calcular área
        area = ((base_mayor + base_menor) * altura) / 2

        # Mostrar resultados
        label_resultado.config(text=f"Altura: {altura:.2f} cm\nPerímetro: {perimetro:.2f} cm\nÁrea: {area:.2f} cm²")

        # Dibujar la figura
        dibujar_trapecio(base_mayor, base_menor, altura, lado3, lado4)

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

def dibujar_trapecio(base_mayor, base_menor, altura, lado3, lado4):
    fig, ax = plt.subplots()

    # Coordenadas de los vértices del trapecio
    x1, y1 = 0, 0
    x2, y2 = base_mayor, 0
    x3, y3 = (base_mayor - base_menor) / 2, altura
    x4, y4 = x3 + base_menor, altura

    # Dibujar el trapecio
    x_coords = [x1, x2, x4, x3, x1]
    y_coords = [y1, y2, y4, y3, y1]
    ax.plot(x_coords, y_coords, 'b-', linewidth=2)
    ax.fill(x_coords, y_coords, 'skyblue', alpha=0.5)

    # Etiquetas
    ax.text(x1, y1, 'A', fontsize=12, color='red')
    ax.text(x2, y2, 'B', fontsize=12, color='red')
    ax.text(x3, y3, 'C', fontsize=12, color='red')
    ax.text(x4, y4, 'D', fontsize=12, color='red')

    ax.set_title("Trapecio Isósceles")
    ax.set_xlabel("cm")
    ax.set_ylabel("cm")
    ax.axis('equal')
    plt.grid()
    plt.show()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Área y Perímetro de un Trapecio")
ventana.geometry("400x400")

# Etiquetas y entradas para las medidas del trapecio
tk.Label(ventana, text="Base Mayor (cm):").pack()
entry_base_mayor = tk.Entry(ventana)
entry_base_mayor.pack()

tk.Label(ventana, text="Base Menor (cm):").pack()
entry_base_menor = tk.Entry(ventana)
entry_base_menor.pack()

tk.Label(ventana, text="Lado Oblicuo 1 (cm):").pack()
entry_lado3 = tk.Entry(ventana)
entry_lado3.pack()

tk.Label(ventana, text="Lado Oblicuo 2 (cm):").pack()
entry_lado4 = tk.Entry(ventana)
entry_lado4.pack()

# Botón para calcular área y perímetro
tk.Button(ventana, text="Calcular", command=calcular).pack(pady=10)

# Etiqueta para mostrar los resultados
label_resultado = tk.Label(ventana, text="", font=("Arial", 12), justify="left")
label_resultado.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()
