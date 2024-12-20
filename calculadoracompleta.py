import tkinter as tk
from tkinter import messagebox

# Función para calcular el PPM a partir de los ml aplicados y volumen del beaker
def calcular_ppm():
    try:
        # Obtener los valores de los campos de entrada
        volumen_beaker = float(entry_volumen_beaker.get())  # Volumen del beaker en litros
        ml_aplicados = float(entry_ml_aplicados.get())  # Mililitros de solución madre aplicados
        
        # Concentración de la solución madre en mg/L
        concentracion_madre = 1476
        
        # Calcular los mg de soluto aplicados
        mg_soluto = ml_aplicados * concentracion_madre  # mg de soluto = ml aplicados * concentración madre
        
        # Calcular el PPM
        ppm = mg_soluto / volumen_beaker  # PPM = mg de soluto / volumen del beaker (en litros)
        label_resultado_ppm.config(text=f"PPM: {ppm:.2f} PPM", bg="#28a745", fg="white", font=("Arial", 10, "bold"), anchor="center")
        
        # Llamar a la función para calcular la solución madre usando el PPM calculado
        calcular_solucion_madre(ppm)

    except ValueError:
        label_resultado_ppm.config(text="Por favor ingresa valores válidos", bg="#dc3545", fg="white", font=("Arial", 10, "bold"), anchor="center")

# Función para calcular la cantidad de solución madre a aplicar según el caudal y PPM deseado
def calcular_solucion_madre(ppm_deseado=None):
    try:
        # Si ppm_deseado es None, usamos el ppm calculado
        if ppm_deseado is None:
            label_resultado_solucion.config(text="Por favor calcula primero el PPM", bg="#dc3545", fg="white", font=("Arial", 10, "bold"), anchor="center")
            return

        # Obtener los valores de los campos de entrada
        caudal_m3h = float(entry_caudal.get())  # Caudal en m³/h
        
        concentracion_madre = 1476  # Concentración de la solución madre en mg/L
        
        # Aplicar la fórmula para calcular los litros de solución madre por hora
        litros_solucion_madre = (ppm_deseado * caudal_m3h) / concentracion_madre
        
        # Convertir metros cúbicos a litros (1 m³ = 1000 litros)
        litros_por_hora = litros_solucion_madre * 1000  # Convertimos de m³ a litros
        
        # Redondear el resultado a 0 decimales
        litros_por_hora_redondeado = round(litros_por_hora)
        
        # Mostrar los resultados en litros por hora (redondeado)
        label_resultado_solucion.config(text=f"Litros de solución madre a aplicar por hora: {litros_por_hora_redondeado} l/h", bg="#28a745", fg="white", font=("Arial", 10, "bold"), anchor="center")
        label_caudal_resultado.config(text=f"Caudal: {caudal_m3h:.2f} m³/h\nPPM deseado: {ppm_deseado:.2f} PPM", bg="#28a745", fg="white", font=("Arial", 10, "bold"), anchor="center")

        # Calcular cuántos centímetros deben bajar según los litros por hora
        cm_bajar = litros_por_hora_redondeado / 11.33  # 1 cm = 11.33 litros
        cm_bajar_redondeado = round(cm_bajar, 2)  # Redondeamos a 2 decimales
        
        # Mostrar el resultado de los centímetros a bajar
        label_resultado_cm.config(text=f"Centímetros a bajar por hora: {cm_bajar_redondeado} cm", bg="#28a745", fg="white", font=("Arial", 10, "bold"), anchor="center")

    except ValueError:
        label_resultado_solucion.config(text="Por favor ingresa valores válidos", bg="#dc3545", fg="white", font=("Arial", 10, "bold"), anchor="center")
        label_caudal_resultado.config(text="", bg="#dc3545", fg="white", font=("Arial", 10, "bold"), anchor="center")

# Función para abrir la ventana de la calculadora de coagulante
def abrir_calculadora_coagulante():
    # Crear una nueva ventana secundaria para la calculadora de coagulante
    ventana_coagulante = tk.Toplevel(ventana)
    ventana_coagulante.title("Calculadora de Gasto de Coagulante")
    ventana_coagulante.geometry("400x450")
    ventana_coagulante.config(bg="#003366")

    # Título de la calculadora de coagulante
    titulo_coagulante = tk.Label(ventana_coagulante, text="Calculadora de Gasto de Coagulante", bg="#003366", font=("Arial", 10, "bold"), fg="white")
    titulo_coagulante.pack(pady=20)

    # Entradas para la calculadora de coagulante
    label_cm = tk.Label(ventana_coagulante, text="Ingrese los cm que bajo el ibc:", bg="#003366", font=("Arial", 10, "bold"), fg="white")
    label_cm.pack()
    entry_cm = tk.Entry(ventana_coagulante, font=("Arial", 10), bg="white")
    entry_cm.pack(pady=5)

    label_min = tk.Label(ventana_coagulante, text="Ingrese los minutos que demoró en bajar el nivel del ibc:", bg="#003366", font=("Arial", 10, "bold"), fg="white")
    label_min.pack()
    entry_min = tk.Entry(ventana_coagulante, font=("Arial", 10), bg="white")
    entry_min.pack(pady=5)

    label_ppm = tk.Label(ventana_coagulante, text="Ingrese las ppm que desea dosificar:", bg="#003366", font=("Arial", 10, "bold"), fg="white")
    label_ppm.pack()
    entry_ppm = tk.Entry(ventana_coagulante, font=("Arial", 10), bg="white")
    entry_ppm.pack(pady=5)

    label_caudal = tk.Label(ventana_coagulante, text="Ingrese el caudal que está trabajando en planta:", bg="#003366", font=("Arial", 10, "bold"), fg="white")
    label_caudal.pack()
    entry_caudal = tk.Entry(ventana_coagulante, font=("Arial", 10), bg="white")
    entry_caudal.pack(pady=5)

    # Función para calcular los litros por hora en la calculadora de coagulante
    def calcular_coagulante():
        try:
            cm = float(entry_cm.get())
            min = float(entry_min.get())
            ppm = float(entry_ppm.get())
            caudal = float(entry_caudal.get())
            
            # Fórmulas
            ibc = 1081 / 94
            bajo = ibc / min
            litrosBomba = ibc / min * 60
            litrosH = ppm * caudal / 1290
            
            # Mostrar los resultados
            label_resultado_coagulante.config(text=f"Los litros * cm son: {bajo:.2f}\n"
                                                   f"Los litros dosificación bomba son: {litrosBomba:.2f} L/h\n"
                                                   f"Los litros por hora cálculo ppm son: {litrosH:.2f} L/h", 
                                                   fg="white", font=("Arial", 10, "bold"), anchor="center")
        
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos para Coagulante.")

    # Botón para calcular el coagulante
    boton_calcular_coagulante = tk.Button(ventana_coagulante, text="Calcular Coagulante", command=calcular_coagulante, bg="#32CD32", fg="white", font=("Arial", 10, "bold"), relief="raised")
    boton_calcular_coagulante.pack(pady=20)

    # Etiqueta para mostrar los resultados de la calculadora de coagulante
    label_resultado_coagulante = tk.Label(ventana_coagulante, text="", bg="#003366", font=("Arial", 10, "bold"), fg="white", anchor="center")
    label_resultado_coagulante.pack(pady=10)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Principal")
ventana.geometry("600x600")
ventana.config(bg="#003366")

# Botón para abrir la calculadora de coagulante (ubicado en la parte superior)
boton_abrir_coagulante = tk.Button(ventana, text="Abrir Calculadora de Coagulante", command=abrir_calculadora_coagulante, font=("Arial", 12, "bold"), bg="#17a2b8", fg="white", relief="raised")
boton_abrir_coagulante.pack(pady=20)

# Título
label_titulo = tk.Label(ventana, text="Calculadora PPM y Coagulante", font=("Arial", 12, "bold"), bg="#003366", fg="white")
label_titulo.pack(pady=20)

# Cálculo de PPM
label_ppm_beaker = tk.Label(ventana, text="Ingrese el volumen del beaker en litros:", bg="#003366", font=("Arial", 10, "bold"), fg="white")
label_ppm_beaker.pack(pady=5)

entry_volumen_beaker = tk.Entry(ventana, font=("Arial", 10), bg="white", bd=2)
entry_volumen_beaker.pack(pady=5)

label_ml_aplicados = tk.Label(ventana, text="Ingrese los ml de solución madre aplicados:", bg="#003366", font=("Arial", 10, "bold"), fg="white")
label_ml_aplicados.pack(pady=5)

entry_ml_aplicados = tk.Entry(ventana, font=("Arial", 10), bg="white", bd=2)
entry_ml_aplicados.pack(pady=5)

# Botón para calcular el PPM
boton_calcular_ppm = tk.Button(ventana, text="Calcular PPM", command=calcular_ppm, font=("Arial", 10, "bold"), bg="#32CD32", fg="white", relief="raised")
boton_calcular_ppm.pack(pady=20)

# Etiqueta para mostrar el resultado del PPM
label_resultado_ppm = tk.Label(ventana, text="PPM: ", bg="#003366", font=("Arial", 10, "bold"), fg="white", anchor="center")
label_resultado_ppm.pack(pady=10)

# Caudal y cálculo de solución madre
label_caudal = tk.Label(ventana, text="Ingrese el caudal en m³/h para solución madre:", bg="#003366", font=("Arial", 10, "bold"), fg="white")
label_caudal.pack(pady=5)

entry_caudal = tk.Entry(ventana, font=("Arial", 10), bg="white", bd=2)
entry_caudal.pack(pady=5)

# Botón para calcular la solución madre
boton_calcular_solucion = tk.Button(ventana, text="Calcular Solución Madre", command=calcular_solucion_madre, font=("Arial", 10, "bold"), bg="#32CD32", fg="white", relief="raised")
boton_calcular_solucion.pack(pady=20)

# Etiqueta para mostrar los resultados de la solución madre
label_resultado_solucion = tk.Label(ventana, text="Resultados solución madre", bg="#003366", font=("Arial", 10, "bold"), fg="white", anchor="center")
label_resultado_solucion.pack(pady=10)

label_caudal_resultado = tk.Label(ventana, text="Resultados del caudal", bg="#003366", font=("Arial", 10, "bold"), fg="white", anchor="center")
label_caudal_resultado.pack(pady=10)

# Iniciar la interfaz
ventana.mainloop()
