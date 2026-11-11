
# INTERFAZ GRAFICA - ACTIVIDAD 5
# ==========================================

# Pantalla de la Actividad 5:
# - Ruta de menor costo entre dos ciudades (Dijkstra).
# - Arbol de recubrimiento minimo entre los seis centros (Prim).
#
# Mantiene el mismo diseno de las partes 1 a 4: encabezado azul,
# formulario blanco, tabla de resultados y area de texto con el detalle.

import tkinter as tk
from tkinter import ttk, messagebox
import time

from parte_5_ruta_arbol_minimo.actividad5 import (
    construir_grafo,
    ruta_mas_corta,
    arbol_recubrimiento_minimo,
    CIUDADES,
    CONEXIONES
)


def iniciar_interfaz5(parent):

    ventana = tk.Toplevel(parent)
    ventana.title("UPN CARGO - Ruta de Entrega y Arbol Minimo")
    ventana.geometry("1100x720")
    ventana.minsize(950, 620)
    ventana.configure(bg="#F1F5F9")

    # El grafo se arma una sola vez, al abrir la ventana.
    grafo = construir_grafo()

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
        text="PARTE 5 - RUTA DE ENTREGA Y ARBOL DE RECUBRIMIENTO MINIMO",
        font=("Arial", 11),
        fg="white",
        bg="#17365D"
    ).pack()

    # ==========================================
    # CONTENIDO PRINCIPAL
    # ==========================================

    contenido = tk.Frame(
        ventana,
        bg="#F1F5F9",
        padx=25,
        pady=20
    )
    contenido.pack(fill="both", expand=True)

    tk.Label(
        contenido,
        text="OPTIMIZACION DE RUTAS ENTRE CIUDADES",
        font=("Arial", 15, "bold"),
        bg="#F1F5F9",
        fg="#17365D"
    ).pack(anchor="w", pady=(0, 12))

    # ==========================================
    # FORMULARIO
    # ==========================================

    formulario = tk.Frame(
        contenido,
        bg="white",
        padx=15,
        pady=15
    )
    formulario.pack(fill="x")

    tk.Label(
        formulario,
        text="Ciudad de origen:",
        font=("Arial", 10, "bold"),
        bg="white"
    ).grid(row=0, column=0, padx=5, pady=5)

    selector_origen = ttk.Combobox(
        formulario,
        state="readonly",
        width=20,
        values=CIUDADES
    )
    selector_origen.current(0)
    selector_origen.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(
        formulario,
        text="Ciudad de destino:",
        font=("Arial", 10, "bold"),
        bg="white"
    ).grid(row=0, column=2, padx=5, pady=5)

    selector_destino = ttk.Combobox(
        formulario,
        state="readonly",
        width=20,
        values=CIUDADES
    )
    selector_destino.current(1)
    selector_destino.grid(row=0, column=3, padx=10, pady=5)

    tk.Label(
        formulario,
        text=f"Centros de distribucion: {len(CIUDADES)} ciudades | "
             f"Tramos registrados: {len(CONEXIONES)}",
        font=("Arial", 10),
        fg="#475569",
        bg="white"
    ).grid(
        row=1,
        column=0,
        columnspan=4,
        sticky="w",
        padx=5,
        pady=(10, 0)
    )

    # ==========================================
    # BOTONES
    # ==========================================

    botones = tk.Frame(
        contenido,
        bg="#F1F5F9"
    )
    botones.pack(fill="x", pady=15)

    # ==========================================
    # TABLA DE TRAMOS
    # ==========================================

    tk.Label(
        contenido,
        text="TRAMOS",
        font=("Arial", 12, "bold"),
        bg="#F1F5F9",
        fg="#17365D"
    ).pack(anchor="w", pady=(0, 5))

    marco_tabla = tk.Frame(contenido)
    marco_tabla.pack(fill="both", expand=True)

    columnas = (
        "tramo",
        "costo",
        "acumulado"
    )

    tabla = ttk.Treeview(
        marco_tabla,
        columns=columnas,
        show="headings",
        height=7
    )

    tabla.heading(
        "tramo",
        text="Tramo"
    )
    tabla.heading(
        "costo",
        text="Costo (km)"
    )
    tabla.heading(
        "acumulado",
        text="Costo acumulado (km)"
    )

    tabla.column(
        "tramo",
        width=380,
        anchor="center"
    )
    tabla.column(
        "costo",
        width=200,
        anchor="center"
    )
    tabla.column(
        "acumulado",
        width=220,
        anchor="center"
    )

    barra_vertical = ttk.Scrollbar(
        marco_tabla,
        orient="vertical",
        command=tabla.yview
    )

    tabla.configure(
        yscrollcommand=barra_vertical.set
    )

    marco_tabla.rowconfigure(0, weight=1)
    marco_tabla.columnconfigure(0, weight=1)

    tabla.grid(
        row=0,
        column=0,
        sticky="nsew"
    )
    barra_vertical.grid(
        row=0,
        column=1,
        sticky="ns"
    )

    # ==========================================
    # AREA DE RESULTADOS
    # ==========================================

    tk.Label(
        contenido,
        text="RESULTADOS",
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
        state="disabled",
        wrap="word"
    )
    resultados.pack(fill="x")

    # ==========================================
    # FUNCIONES DE PRESENTACION
    # ==========================================

    def limpiar_tabla():

        for elemento in tabla.get_children():
            tabla.delete(elemento)

    def escribir_resultados(texto):

        resultados.configure(state="normal")
        resultados.delete("1.0", "end")
        resultados.insert("end", texto)
        resultados.configure(state="disabled")

    def insertar_tramo(tramo, costo, acumulado):

        tabla.insert(
            "",
            "end",
            values=(
                tramo,
                costo,
                acumulado
            )
        )

    # ==========================================
    # BUSCAR RUTA ENTRE DOS CIUDADES
    # ==========================================

    def buscar_ruta():

        origen = selector_origen.get()
        destino = selector_destino.get()

        if origen == destino:
            messagebox.showwarning(
                "Ruta",
                "Seleccione dos ciudades diferentes.",
                parent=ventana
            )
            return

        # 1. Se calcula la ruta y se mide cuanto tarda.
        inicio = time.perf_counter()

        camino, costo_total = ruta_mas_corta(grafo, origen, destino)

        tiempo = time.perf_counter() - inicio

        limpiar_tabla()

        if camino is None:

            escribir_resultados(
                f"No existe una ruta entre {origen} y {destino}."
            )
            return

        # 2. Se llena la tabla con cada tramo del camino encontrado.
        acumulado = 0

        for posicion in range(len(camino) - 1):

            tramo_origen = camino[posicion]
            tramo_destino = camino[posicion + 1]

            costo_tramo = grafo[tramo_origen][tramo_destino]
            acumulado = acumulado + costo_tramo

            insertar_tramo(
                f"{tramo_origen} -> {tramo_destino}",
                costo_tramo,
                acumulado
            )

        lineas = [
            f"RUTA MAS CORTA: {origen} -> {destino}",
            " -> ".join(camino),
            "",
            f"Tramos recorridos: {len(camino) - 1}",
            f"Costo total del envio: {costo_total} km",
            f"Tiempo de ejecucion: {tiempo:.8f} segundos",
            "",
            "METODO UTILIZADO:",
            "Algoritmo de Dijkstra.",
            "En cada paso se visita la ciudad pendiente con el menor",
            "costo acumulado y se actualizan sus ciudades vecinas."
        ]

        escribir_resultados("\n".join(lineas))

    # ==========================================
    # ARBOL DE RECUBRIMIENTO MINIMO
    # ==========================================

    def calcular_arbol_minimo():

        # 1. Se calcula el arbol y se mide cuanto tarda.
        inicio = time.perf_counter()

        aristas, costo_total = arbol_recubrimiento_minimo(grafo)

        tiempo = time.perf_counter() - inicio

        limpiar_tabla()

        # 2. Se llena la tabla con los tramos elegidos por el algoritmo.
        acumulado = 0

        for origen, destino, costo_tramo in aristas:

            acumulado = acumulado + costo_tramo

            insertar_tramo(
                f"{origen} - {destino}",
                costo_tramo,
                acumulado
            )

        lineas = [
            "ARBOL DE RECUBRIMIENTO MINIMO",
            "",
            f"Ciudades conectadas: {len(aristas) + 1}",
            f"Tramos seleccionados: {len(aristas)}",
            f"Costo total de la red: {costo_total} km",
            f"Ahorro frente a todas las conexiones: "
            f"{sum(costo for _, _, costo in CONEXIONES) - costo_total} km",
            f"Tiempo de ejecucion: {tiempo:.8f} segundos",
            "",
            "METODO UTILIZADO:",
            "Algoritmo de Prim.",
            "Se parte de una ciudad y se agrega siempre el tramo mas",
            "barato que conecta el arbol con una ciudad nueva."
        ]

        escribir_resultados("\n".join(lineas))

    # ==========================================
    # LIMPIAR RESULTADOS
    # ==========================================

    def limpiar_resultados():

        limpiar_tabla()

        selector_origen.current(0)
        selector_destino.current(1)

        escribir_resultados(
            "Seleccione las ciudades y presione BUSCAR RUTA, "
            "o calcule el ARBOL DE RECUBRIMIENTO MINIMO."
        )

    # ==========================================
    # CONFIGURACION DE BOTONES
    # ==========================================

    tk.Button(
        botones,
        text="BUSCAR RUTA",
        command=buscar_ruta,
        bg="#2563EB",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=15,
        pady=8
    ).pack(side="left", padx=(0, 10))

    tk.Button(
        botones,
        text="ARBOL DE RECUBRIMIENTO MINIMO",
        command=calcular_arbol_minimo,
        bg="#15803D",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=15,
        pady=8
    ).pack(side="left", padx=10)

    tk.Button(
        botones,
        text="LIMPIAR RESULTADOS",
        command=limpiar_resultados,
        bg="#475569",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=15,
        pady=8
    ).pack(side="left", padx=10)

    # ==========================================
    # ESTADO INICIAL
    # ==========================================

    limpiar_resultados()

    ventana.transient(parent)

    return ventana


# ==========================================
# EJECUCION INDEPENDIENTE
# ==========================================

if __name__ == "__main__":

    raiz = tk.Tk()
    raiz.withdraw()

    ventana = iniciar_interfaz5(raiz)

    ventana.protocol(
        "WM_DELETE_WINDOW",
        raiz.destroy
    )

    raiz.mainloop()
