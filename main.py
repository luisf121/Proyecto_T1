import tkinter as tk

# Crear ventana
ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("350x200")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese su nombre:")
etiqueta.pack(pady=10)

# Campo de texto
entrada = tk.Entry(ventana)
entrada.pack()

# Función del botón
def saludar():
    nombre = entrada.get()
    resultado.config(text="¡Hola " + nombre + "!")

# Botón
boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack(pady=10)

# Resultado
resultado = tk.Label(ventana, text="")
resultado.pack()

# Ejecutar ventana
ventana.mainloop()