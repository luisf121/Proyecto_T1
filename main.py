
# SISTEMA UPN CARGO S.A.C.

import tkinter as tk
from tkinter import ttk

# IMPORTAR INTERFACES
from parte_1_estructura_datos.interfaz1 import iniciar_interfaz
from parte_2_busquedas.interfaz2 import iniciar_interfaz2
from parte_3_ordenamiento.interfaz3 import iniciar_interfaz3
from parte_4_algoritmos_voraces.interfaz4 import iniciar_interfaz4
from parte_5_ruta_arbol_minimo.interfaz5 import iniciar_interfaz5


def main():

    # VENTANA PRINCIPAL
    ventana = tk.Tk()
    ventana.title("UPN CARGO S.A.C. - Sistema de Gestion Logistica")
    ventana.geometry("750x720")
    ventana.configure(bg="#F1F5F9")
    ventana.resizable(False, False)

    # ENCABEZADO
    encabezado = tk.Frame(
        ventana,
        bg="#17365D",
        height=130
    )
    encabezado.pack(fill="x")

    tk.Label(
        encabezado,
        text="UPN CARGO S.A.C.",
        font=("Arial", 26, "bold"),
        fg="white",
        bg="#17365D"
    ).pack(pady=(25, 5))

    tk.Label(
        encabezado,
        text="SISTEMA DE GESTION LOGISTICA",
        font=("Arial", 12),
        fg="white",
        bg="#17365D"
    ).pack()

    # CONTENIDO PRINCIPAL
    contenido = tk.Frame(
        ventana,
        bg="#F1F5F9"
    )
    contenido.pack(fill="both", expand=True)

    tk.Label(
        contenido,
        text="MENU PRINCIPAL",
        font=("Arial", 20, "bold"),
        fg="#17365D",
        bg="#F1F5F9"
    ).pack(pady=(35, 10))

    tk.Label(
        contenido,
        text="Seleccione la actividad que desea ejecutar:",
        font=("Arial", 11),
        bg="#F1F5F9",
        fg="#334155"
    ).pack(pady=10)

    # BOTON ACTIVIDAD 1
    ttk.Button(
        contenido,
        text="ACTIVIDAD 1 - ESTRUCTURAS DE DATOS",
        command=lambda: iniciar_interfaz(ventana)
    ).pack(pady=12, ipadx=25, ipady=10)

    # BOTON ACTIVIDAD 2
    ttk.Button(
        contenido,
        text="ACTIVIDAD 2 - ALGORITMOS DE BUSQUEDA",
        command=lambda: iniciar_interfaz2(ventana)
    ).pack(pady=12, ipadx=25, ipady=10)
    # BOTON ACTIVIDAD 3
    ttk.Button(
        contenido,
        text="ACTIVIDAD 3 - ALGORITMOS DE ORDENAMIENTO",
        command=lambda: iniciar_interfaz3(ventana)
    ).pack(pady=10, ipadx=25, ipady=8)

    # BOTON ACTIVIDAD 4
    ttk.Button(
        contenido,
        text="ACTIVIDAD 4 - ALGORITMOS VORACES",
        command=lambda: iniciar_interfaz4(ventana)
    ).pack(pady=10, ipadx=25, ipady=8)
    # BOTON ACTIVIDAD 5
    ttk.Button(
        contenido,
        text="ACTIVIDAD 5 - RUTA Y ARBOL DE RECUBRIMIENTO MINIMO",
        command=lambda: iniciar_interfaz5(ventana)
    ).pack(pady=10, ipadx=25, ipady=8)
    # PIE DE PAGINA
    tk.Label(
        ventana,
        text="Desarrollo de Evaluación T1 | Grupo 9",
        font=("Arial", 9),
        fg="#64748B",
        bg="#F1F5F9"
    ).pack(side="bottom", pady=15)
    
    
    # EJECUTAR SISTEMA
    ventana.mainloop()


if __name__ == "__main__":
    main()
