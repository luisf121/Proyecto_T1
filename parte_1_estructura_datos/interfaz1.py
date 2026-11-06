
# INTERFAZ GRAFICA - ACTIVIDAD 1


import tkinter as tk
from tkinter import ttk, messagebox

from parte_1_estructura_datos.actividad1 import (
    pedidos,
    buscar_por_cliente
)


def iniciar_interfaz():

    ventana = tk.Tk()
    ventana.title("UPN CARGO S.A.C. - Gestion de Pedidos")
    ventana.geometry("1050x600")
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
        text="SISTEMA DE GESTION LOGISTICA",
        font=("Arial", 11),
        fg="white",
        bg="#17365D"
    ).pack()

    # CONTENEDOR PRINCIPAL
    contenido = tk.Frame(ventana, bg="#F1F5F9", padx=25, pady=20)
    contenido.pack(fill="both", expand=True)

    tk.Label(
        contenido,
        text="ACTIVIDAD 1: REGISTRO Y BUSQUEDA DE PEDIDOS",
        font=("Arial", 15, "bold"),
        bg="#F1F5F9",
        fg="#17365D"
    ).pack(anchor="w", pady=(0, 15))

    # AREA DE BUSQUEDA
    marco_busqueda = tk.Frame(contenido, bg="white", padx=15, pady=15)
    marco_busqueda.pack(fill="x", pady=5)

    tk.Label(
        marco_busqueda,
        text="Nombre del cliente:",
        font=("Arial", 11),
        bg="white"
    ).pack(side="left", padx=5)

    entrada_nombre = tk.Entry(
        marco_busqueda,
        font=("Arial", 11),
        width=30
    )
    entrada_nombre.pack(side="left", padx=10)

    # TABLA DE PEDIDOS
    columnas = ("codigo", "cliente", "ciudad", "peso", "prioridad", "costo")

    tabla = ttk.Treeview(
        contenido,
        columns=columnas,
        show="headings",
        height=13
    )

    encabezados = {
        "codigo": "CODIGO",
        "cliente": "CLIENTE",
        "ciudad": "CIUDAD",
        "peso": "PESO (KG)",
        "prioridad": "PRIORIDAD",
        "costo": "COSTO (S/.)"
    }

    anchos = {
        "codigo": 90,
        "cliente": 200,
        "ciudad": 150,
        "peso": 100,
        "prioridad": 120,
        "costo": 120
    }

    for columna in columnas:
        tabla.heading(columna, text=encabezados[columna])
        tabla.column(columna, width=anchos[columna], anchor="center")

    tabla.pack(fill="both", expand=True, pady=15)

    # ETIQUETA DE RESULTADOS
    etiqueta_resultado = tk.Label(
        contenido,
        text="Total de pedidos registrados: 15",
        font=("Arial", 10, "bold"),
        bg="#F1F5F9",
        fg="#17365D"
    )
    etiqueta_resultado.pack(anchor="w")

    # FUNCION PARA MOSTRAR PEDIDOS
    def mostrar_pedidos(lista):

        for fila in tabla.get_children():
            tabla.delete(fila)

        for pedido in lista:
            tabla.insert(
                "",
                "end",
                values=(
                    pedido["codigo"],
                    pedido["cliente"],
                    pedido["ciudad"],
                    pedido["peso"],
                    pedido["prioridad"],
                    f'{pedido["costo"]:.2f}'
                )
            )

        etiqueta_resultado.config(
            text=f"Total de pedidos encontrados: {len(lista)}"
        )

    # FUNCION DEL BOTON BUSCAR
    def ejecutar_busqueda():

        nombre = entrada_nombre.get().strip()

        if not nombre:
            messagebox.showwarning(
                "Busqueda",
                "Ingrese el nombre o parte del nombre del cliente."
            )
            return

        resultados = buscar_por_cliente(pedidos, nombre)

        mostrar_pedidos(resultados)

        if not resultados:
            messagebox.showinfo(
                "Resultado",
                "No se encontraron pedidos."
            )

    # FUNCION DEL BOTON LIMPIAR
    def limpiar_busqueda():

        entrada_nombre.delete(0, tk.END)
        mostrar_pedidos(pedidos)

    # BOTONES
    tk.Button(
        marco_busqueda,
        text="BUSCAR",
        command=ejecutar_busqueda,
        bg="#2563EB",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=15
    ).pack(side="left", padx=5)

    tk.Button(
        marco_busqueda,
        text="LIMPIAR",
        command=limpiar_busqueda,
        bg="#64748B",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=15
    ).pack(side="left", padx=5)

    # MOSTRAR LOS 15 PEDIDOS AL INICIAR
    mostrar_pedidos(pedidos)

    ventana.mainloop()
