
# INTERFAZ GRAFICA - ACTIVIDAD 2

import tkinter as tk
from tkinter import ttk, messagebox
import time

from parte_1_estructura_datos.actividad1 import pedidos

from parte_2_busquedas.actividad2 import (
    busqueda_lineal,
    busqueda_lineal_acotada,
    busqueda_binaria_iterativa,
    busqueda_binaria_recursiva,
    pedidos_ordenados
)


def iniciar_interfaz2(parent):

    # CREAR VENTANA SECUNDARIA
    ventana = tk.Toplevel(parent)
    ventana.title("UPN CARGO - Algoritmos de Busqueda")
    ventana.geometry("1050x650")
    ventana.configure(bg="#F1F5F9")

    # ENCABEZADO
    encabezado = tk.Frame(ventana, bg="#17365D", height=100)
    encabezado.pack(fill="x")

    tk.Label(
        encabezado,
        text="UPN CARGO S.A.C.",
        font=("Arial", 22, "bold"),
        fg="white",
        bg="#17365D"
    ).pack(pady=(15, 5))

    tk.Label(
        encabezado,
        text="PARTE 2 - ALGORITMOS DE BUSQUEDA",
        font=("Arial", 11),
        fg="white",
        bg="#17365D"
    ).pack()

    # CONTENIDO
    contenido = tk.Frame(
        ventana,
        bg="#F1F5F9",
        padx=25,
        pady=20
    )
    contenido.pack(fill="both", expand=True)

    tk.Label(
        contenido,
        text="LOCALIZACION DE PEDIDOS POR CODIGO",
        font=("Arial", 15, "bold"),
        bg="#F1F5F9",
        fg="#17365D"
    ).pack(anchor="w", pady=10)

    # FORMULARIO
    formulario = tk.Frame(
        contenido,
        bg="white",
        padx=15,
        pady=15
    )
    formulario.pack(fill="x")

    tk.Label(
        formulario,
        text="Codigo del pedido:",
        bg="white",
        font=("Arial", 10, "bold")
    ).grid(row=0, column=0, padx=5, pady=8)

    entrada_codigo = tk.Entry(
        formulario,
        font=("Arial", 11),
        width=18
    )
    entrada_codigo.grid(row=0, column=1, padx=5)

    tk.Label(
        formulario,
        text="Algoritmo:",
        bg="white",
        font=("Arial", 10, "bold")
    ).grid(row=0, column=2, padx=5)

    selector = ttk.Combobox(
        formulario,
        state="readonly",
        width=28,
        values=[
            "Busqueda Lineal",
            "Busqueda Lineal Acotada",
            "Busqueda Binaria Iterativa",
            "Busqueda Binaria Recursiva"
        ]
    )
    selector.current(0)
    selector.grid(row=0, column=3, padx=5)

    tk.Label(
        formulario,
        text="Limite:",
        bg="white"
    ).grid(row=1, column=0, padx=5, pady=8)

    entrada_limite = tk.Entry(
        formulario,
        font=("Arial", 10),
        width=10
    )
    entrada_limite.insert(0, "15")
    entrada_limite.grid(row=1, column=1, padx=5, sticky="w")

    # AREA DE RESULTADOS
    tk.Label(
        contenido,
        text="RESULTADOS",
        font=("Arial", 12, "bold"),
        bg="#F1F5F9",
        fg="#17365D"
    ).pack(anchor="w", pady=(20, 5))

    resultados = tk.Text(
        contenido,
        height=15,
        font=("Consolas", 10),
        bg="white",
        relief="solid",
        borderwidth=1
    )
    resultados.pack(fill="both", expand=True)

    # FUNCION PARA MOSTRAR RESULTADOS
    def mostrar_resultado(nombre, pedido, tiempo):

        resultados.insert("end", f"\n{nombre}\n")
        resultados.insert("end", "-" * 55 + "\n")

        if pedido:
            resultados.insert("end", f"Codigo: {pedido['codigo']}\n")
            resultados.insert("end", f"Cliente: {pedido['cliente']}\n")
            resultados.insert("end", f"Ciudad: {pedido['ciudad']}\n")
            resultados.insert("end", f"Peso: {pedido['peso']} kg\n")
            resultados.insert("end", f"Prioridad: {pedido['prioridad']}\n")
            resultados.insert("end", f"Costo: S/. {pedido['costo']:.2f}\n")
        else:
            resultados.insert("end", "Pedido no encontrado.\n")

        resultados.insert(
            "end",
            f"Tiempo de ejecucion: {tiempo:.8f} segundos\n"
        )

    # FUNCION PARA EJECUTAR UN ALGORITMO
    def ejecutar_busqueda():

        codigo = entrada_codigo.get().strip().upper()
        algoritmo = selector.get()

        if not codigo:
            messagebox.showwarning(
                "Validacion",
                "Ingrese el codigo del pedido.",
                parent=ventana
            )
            return

        # Validar limite solo para busqueda acotada
        limite = None

        if algoritmo == "Busqueda Lineal Acotada":

            try:
                limite = int(entrada_limite.get())

                if limite < 0:
                    raise ValueError

            except ValueError:
                messagebox.showerror(
                    "Error",
                    "Ingrese un limite entero no negativo.",
                    parent=ventana
                )
                return

        inicio = time.perf_counter()

        if algoritmo == "Busqueda Lineal":
            pedido = busqueda_lineal(pedidos, codigo)

        elif algoritmo == "Busqueda Lineal Acotada":
            pedido = busqueda_lineal_acotada(
                pedidos, codigo, limite
            )

        elif algoritmo == "Busqueda Binaria Iterativa":
            pedido = busqueda_binaria_iterativa(
                pedidos_ordenados, codigo
            )

        else:
            pedido = busqueda_binaria_recursiva(
                pedidos_ordenados, codigo
            )

        fin = time.perf_counter()
        tiempo = fin - inicio

        resultados.delete("1.0", "end")
        mostrar_resultado(algoritmo, pedido, tiempo)

    # FUNCION PARA COMPARAR LOS CUATRO ALGORITMOS
    def comparar_algoritmos():

        codigo = entrada_codigo.get().strip().upper()

        if not codigo:
            messagebox.showwarning(
                "Validacion",
                "Ingrese el codigo del pedido.",
                parent=ventana
            )
            return

        try:
            limite = int(entrada_limite.get())

            if limite < 0:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Error",
                "Ingrese un limite entero no negativo.",
                parent=ventana
            )
            return

        algoritmos = [
            ("Busqueda Lineal",
             lambda: busqueda_lineal(pedidos, codigo)),

            ("Busqueda Lineal Acotada",
             lambda: busqueda_lineal_acotada(
                 pedidos, codigo, limite
             )),

            ("Busqueda Binaria Iterativa",
             lambda: busqueda_binaria_iterativa(
                 pedidos_ordenados, codigo
             )),

            ("Busqueda Binaria Recursiva",
             lambda: busqueda_binaria_recursiva(
                 pedidos_ordenados, codigo
             ))
        ]

        resultados.delete("1.0", "end")
        resultados.insert(
            "end",
            f"COMPARACION DE ALGORITMOS PARA: {codigo}\n"
        )
        resultados.insert("end", "=" * 65 + "\n")

        for nombre, funcion in algoritmos:

            inicio = time.perf_counter()
            pedido = funcion()
            fin = time.perf_counter()

            tiempo = fin - inicio

            resultados.insert("end", f"\n{nombre}\n")
            resultados.insert("end", "-" * 45 + "\n")

            if pedido:
                resultados.insert(
                    "end",
                    f"Pedido encontrado: {pedido['codigo']} - "
                    f"{pedido['cliente']}\n"
                )
            else:
                resultados.insert(
                    "end",
                    "Pedido no encontrado.\n"
                )

            resultados.insert(
                "end",
                f"Tiempo: {tiempo:.8f} segundos\n"
            )

    # BOTONES
    botones = tk.Frame(contenido, bg="#F1F5F9")
    botones.pack(pady=15)

    tk.Button(
        botones,
        text="BUSCAR PEDIDO",
        command=ejecutar_busqueda,
        bg="#2563EB",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=15,
        pady=8
    ).pack(side="left", padx=10)

    tk.Button(
        botones,
        text="COMPARAR ALGORITMOS",
        command=comparar_algoritmos,
        bg="#15803D",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=15,
        pady=8
    ).pack(side="left", padx=10)

    # VINCULAR VENTANA SECUNDARIA AL MENU PRINCIPAL
    ventana.transient(parent)
