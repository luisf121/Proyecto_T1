# INTERFAZ GRÁFICA - ACTIVIDAD 3
# ==========================================

import tkinter as tk
from tkinter import ttk, messagebox
import time

from parte_1_estructura_datos.actividad1 import pedidos

from parte_3_ordenamientos.actividad3 import (
    ordenamiento_burbuja,
    ordenamiento_seleccion,
    ordenamiento_insercion
)


def iniciar_interfaz3(parent):

    ventana = tk.Toplevel(parent)
    ventana.title("UPN CARGO - Algoritmos de Ordenamiento")
    ventana.geometry("1100x700")
    ventana.minsize(950, 600)
    ventana.configure(bg="#F1F5F9")

    # ==========================================
    # ENCABEZADO
    # ==========================================

    encabezado = tk.Frame(
        ventana,
        bg="#17365D",
        pady=15
    )
    encabezado.pack(fill="x")

    tk.Label(
        encabezado,
        text="UPN CARGO S.A.C.",
        font=("Arial", 22, "bold"),
        fg="white",
        bg="#17365D"
    ).pack(pady=(0, 5))

    tk.Label(
        encabezado,
        text="PARTE 3 - ALGORITMOS DE ORDENAMIENTO",
        font=("Arial", 11),
        fg="white",
        bg="#17365D"
    ).pack()

    contenido = tk.Frame(
        ventana,
        bg="#F1F5F9",
        padx=25,
        pady=20
    )
    contenido.pack(fill="both", expand=True)

    # ==========================================
    # FORMULARIO
    # ==========================================

    tk.Label(
        contenido,
        text="ORDENAMIENTO DE PEDIDOS POR COSTO DE ENVÍO",
        font=("Arial", 15, "bold"),
        bg="#F1F5F9",
        fg="#17365D"
    ).pack(anchor="w", pady=(0, 12))

    formulario = tk.Frame(
        contenido,
        bg="white",
        padx=15,
        pady=15
    )
    formulario.pack(fill="x")

    tk.Label(
        formulario,
        text="Algoritmo:",
        font=("Arial", 10, "bold"),
        bg="white"
    ).grid(row=0, column=0, padx=5, pady=5)

    selector = ttk.Combobox(
        formulario,
        state="readonly",
        width=30,
        values=[
            "Ordenamiento Burbuja",
            "Ordenamiento por Selección",
            "Ordenamiento por Inserción"
        ]
    )
    selector.current(0)
    selector.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(
        formulario,
        text="Criterio: costo de envío, de menor a mayor",
        font=("Arial", 10),
        fg="#475569",
        bg="white"
    ).grid(row=0, column=2, padx=15, pady=5)

    # ==========================================
    # BOTONES
    # ==========================================

    botones = tk.Frame(
        contenido,
        bg="#F1F5F9"
    )
    botones.pack(fill="x", pady=15)

    # ==========================================
    # TABLA DE PEDIDOS
    # ==========================================

    tk.Label(
        contenido,
        text="PEDIDOS",
        font=("Arial", 12, "bold"),
        bg="#F1F5F9",
        fg="#17365D"
    ).pack(anchor="w", pady=(0, 5))

    marco_tabla = tk.Frame(contenido)
    marco_tabla.pack(fill="both", expand=True)

    columnas = (
        "codigo",
        "cliente",
        "ciudad",
        "peso",
        "prioridad",
        "costo"
    )

    tabla = ttk.Treeview(
        marco_tabla,
        columns=columnas,
        show="headings",
        height=10
    )

    tabla.heading("codigo", text="Código")
    tabla.heading("cliente", text="Cliente")
    tabla.heading("ciudad", text="Ciudad")
    tabla.heading("peso", text="Peso (kg)")
    tabla.heading("prioridad", text="Prioridad")
    tabla.heading("costo", text="Costo (S/)")

    tabla.column("codigo", width=110, anchor="center")
    tabla.column("cliente", width=230, anchor="w")
    tabla.column("ciudad", width=150, anchor="center")
    tabla.column("peso", width=100, anchor="center")
    tabla.column("prioridad", width=110, anchor="center")
    tabla.column("costo", width=120, anchor="e")

    barra_vertical = ttk.Scrollbar(
        marco_tabla,
        orient="vertical",
        command=tabla.yview
    )

    barra_horizontal = ttk.Scrollbar(
        marco_tabla,
        orient="horizontal",
        command=tabla.xview
    )

    tabla.configure(
        yscrollcommand=barra_vertical.set,
        xscrollcommand=barra_horizontal.set
    )

    marco_tabla.rowconfigure(0, weight=1)
    marco_tabla.columnconfigure(0, weight=1)

    tabla.grid(row=0, column=0, sticky="nsew")
    barra_vertical.grid(row=0, column=1, sticky="ns")
    barra_horizontal.grid(row=1, column=0, sticky="ew")

    # ==========================================
    # ÁREA DE RESULTADOS
    # ==========================================

    tk.Label(
        contenido,
        text="RESULTADOS Y COMPARACIÓN",
        font=("Arial", 12, "bold"),
        bg="#F1F5F9",
        fg="#17365D"
    ).pack(anchor="w", pady=(15, 5))

    resultados = tk.Text(
        contenido,
        height=7,
        font=("Consolas", 10),
        bg="white",
        relief="solid",
        borderwidth=1,
        state="disabled"
    )
    resultados.pack(fill="x")

    # ==========================================
    # FUNCIONES DE PRESENTACIÓN
    # ==========================================

    def mostrar_pedidos(lista):

        for elemento in tabla.get_children():
            tabla.delete(elemento)

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
                    f"{pedido['costo']:.2f}"
                )
            )

    def escribir_resultados(texto):

        resultados.configure(state="normal")
        resultados.delete("1.0", "end")
        resultados.insert("end", texto)
        resultados.configure(state="disabled")

    def validar_pedidos():

        if not pedidos:
            messagebox.showwarning(
                "Validación",
                "No hay pedidos registrados para ordenar.",
                parent=ventana
            )
            return False

        return True

    # ==========================================
    # ORDENAR CON EL ALGORITMO SELECCIONADO
    # ==========================================

    def ejecutar_ordenamiento():

        if not validar_pedidos():
            return

        nombre = selector.get()

        funciones = {
            "Ordenamiento Burbuja": ordenamiento_burbuja,
            "Ordenamiento por Selección": ordenamiento_seleccion,
            "Ordenamiento por Inserción": ordenamiento_insercion
        }

        funcion = funciones[nombre]
        datos = pedidos.copy()

        inicio = time.perf_counter()
        lista_ordenada = funcion(datos)
        tiempo = time.perf_counter() - inicio

        mostrar_pedidos(lista_ordenada)

        texto = (
            f"Algoritmo: {nombre}\n"
            f"Pedidos ordenados: {len(lista_ordenada)}\n"
            f"Orden: costo de envío de menor a mayor\n"
            f"Tiempo de ejecución: {tiempo:.8f} segundos\n"
            f"Menor costo: S/ {lista_ordenada[0]['costo']:.2f}\n"
            f"Mayor costo: S/ {lista_ordenada[-1]['costo']:.2f}"
        )

        escribir_resultados(texto)

    # ==========================================
    # COMPARAR LOS TRES ALGORITMOS
    # ==========================================

    def comparar_algoritmos():

        if not validar_pedidos():
            return

        algoritmos = [
            ("Burbuja", ordenamiento_burbuja),
            ("Selección", ordenamiento_seleccion),
            ("Inserción", ordenamiento_insercion)
        ]

        repeticiones = 30
        lineas = [
            f"COMPARACIÓN CON {len(pedidos)} PEDIDOS",
            f"Promedio de {repeticiones} ejecuciones por algoritmo",
            "-" * 65
        ]

        for nombre, funcion in algoritmos:

            tiempo_total = 0.0

            for _ in range(repeticiones):

                datos = pedidos.copy()

                inicio = time.perf_counter()
                lista_ordenada = funcion(datos)
                tiempo_total += time.perf_counter() - inicio

            tiempo_promedio = tiempo_total / repeticiones

            lineas.append(
                f"{nombre:<15} "
                f"Tiempo promedio: {tiempo_promedio:.8f} segundos"
            )

        lineas.append(
            "Tiempos orientativos; cada ejecución recibe los mismos datos."
        )

        escribir_resultados("\n".join(lineas))

    # ==========================================
    # MOSTRAR EL ORDEN ORIGINAL
    # ==========================================

    def mostrar_originales():

        mostrar_pedidos(pedidos)

        escribir_resultados(
            f"Se muestran {len(pedidos)} pedidos en su orden original."
        )

    # ==========================================
    # CONFIGURACIÓN DE BOTONES
    # ==========================================

    tk.Button(
        botones,
        text="ORDENAR PEDIDOS",
        command=ejecutar_ordenamiento,
        bg="#2563EB",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=15,
        pady=8
    ).pack(side="left", padx=(0, 10))

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

    tk.Button(
        botones,
        text="VER ORDEN ORIGINAL",
        command=mostrar_originales,
        bg="#475569",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=15,
        pady=8
    ).pack(side="left", padx=10)

    mostrar_originales()

    ventana.transient(parent)

    return ventana


# ==========================================
# EJECUCIÓN INDEPENDIENTE
# ==========================================

if __name__ == "__main__":

    raiz = tk.Tk()
    raiz.withdraw()

    ventana = iniciar_interfaz3(raiz)
    ventana.protocol("WM_DELETE_WINDOW", raiz.destroy)

    raiz.mainloop()
