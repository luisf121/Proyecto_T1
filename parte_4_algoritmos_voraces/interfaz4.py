
# INTERFAZ GRAFICA - ACTIVIDAD 4
# ==========================================

import tkinter as tk
from tkinter import ttk, messagebox
import time

from parte_4_algoritmos_voraces.actividad4 import (
    calcular_billetes,
    BILLETES,
    MONTOS
)


def iniciar_interfaz4(parent):

    ventana = tk.Toplevel(parent)
    ventana.title("UPN CARGO - Algoritmos Voraces")
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
        text="PARTE 4 - ALGORITMOS VORACES",
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
        text="OPTIMIZACION DE ENTREGA DE VIATICOS",
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
        text="Monto de viaticos:",
        font=("Arial", 10, "bold"),
        bg="white"
    ).grid(row=0, column=0, padx=5, pady=5)

    selector = ttk.Combobox(
        formulario,
        state="readonly",
        width=25,
        values=[f"S/ {monto}" for monto in MONTOS]
    )
    selector.current(0)
    selector.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(
        formulario,
        text="Seleccionar la menor cantidad de billetes",
        font=("Arial", 10),
        fg="#475569",
        bg="white"
    ).grid(row=0, column=2, padx=15, pady=5)

    tk.Label(
        formulario,
        text="Denominaciones disponibles: "
             + ", ".join(f"S/ {b}" for b in BILLETES),
        font=("Arial", 10),
        fg="#475569",
        bg="white"
    ).grid(
        row=1,
        column=0,
        columnspan=3,
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
    # TABLA DE BILLETES
    # ==========================================

    tk.Label(
        contenido,
        text="DISTRIBUCION DE BILLETES",
        font=("Arial", 12, "bold"),
        bg="#F1F5F9",
        fg="#17365D"
    ).pack(anchor="w", pady=(0, 5))

    marco_tabla = tk.Frame(contenido)
    marco_tabla.pack(fill="both", expand=True)

    columnas = (
        "denominacion",
        "cantidad",
        "subtotal"
    )

    tabla = ttk.Treeview(
        marco_tabla,
        columns=columnas,
        show="headings",
        height=8
    )

    tabla.heading(
        "denominacion",
        text="Denominacion (S/)"
    )
    tabla.heading(
        "cantidad",
        text="Cantidad de billetes"
    )
    tabla.heading(
        "subtotal",
        text="Subtotal (S/)"
    )

    tabla.column(
        "denominacion",
        width=250,
        anchor="center"
    )
    tabla.column(
        "cantidad",
        width=250,
        anchor="center"
    )
    tabla.column(
        "subtotal",
        width=250,
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
        text="RESULTADOS DEL ALGORITMO VORAZ",
        font=("Arial", 12, "bold"),
        bg="#F1F5F9",
        fg="#17365D"
    ).pack(anchor="w", pady=(15, 5))

    resultados = tk.Text(
        contenido,
        height=8,
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

    def mostrar_distribucion(distribucion):

        limpiar_tabla()

        for billete, cantidad in distribucion.items():

            subtotal = billete * cantidad

            tabla.insert(
                "",
                "end",
                values=(
                    f"S/ {billete}",
                    cantidad,
                    f"S/ {subtotal}"
                )
            )

    def obtener_monto():

        seleccion = selector.get()
        return int(seleccion.replace("S/", "").strip())

    # ==========================================
    # EJECUTAR ALGORITMO VORAZ
    # ==========================================

    def ejecutar_voraz():

        try:
            monto = obtener_monto()

            inicio = time.perf_counter()

            distribucion, restante = calcular_billetes(monto)

            tiempo = time.perf_counter() - inicio

            mostrar_distribucion(distribucion)

            total_billetes = sum(distribucion.values())

            lineas = [
                f"Monto solicitado: S/ {monto}",
                f"Total de billetes utilizados: {total_billetes}",
                f"Monto restante: S/ {restante}",
                f"Tiempo de ejecucion: {tiempo:.8f} segundos",
                "",
                "PROCEDIMIENTO VORAZ:",
                "Se seleccionan los billetes de mayor a menor."
            ]

            for billete, cantidad in distribucion.items():
                lineas.append(
                    f"{cantidad} billete(s) de S/ {billete} "
                    f"= S/ {billete * cantidad}"
                )

            if restante == 0:
                lineas.append(
                    "\nResultado: monto distribuido correctamente."
                )
            else:
                lineas.append(
                    "\nResultado: quedo un monto sin distribuir."
                )

            escribir_resultados("\n".join(lineas))

        except (ValueError, IndexError):
            messagebox.showerror(
                "Error",
                "Seleccione un monto valido.",
                parent=ventana
            )

    # ==========================================
    # MOSTRAR LOS TRES CASOS
    # ==========================================

    def comparar_montos():

        lineas = [
            "COMPARACION DE MONTOS DE VIATICOS",
            "-" * 55
        ]

        for monto in MONTOS:

            distribucion, restante = calcular_billetes(monto)

            total = sum(distribucion.values())

            detalle = ", ".join(
                f"{cantidad} x S/ {billete}"
                for billete, cantidad in distribucion.items()
            )

            lineas.append(
                f"Monto: S/ {monto} | "
                f"Billetes: {total} | "
                f"Restante: S/ {restante}"
            )

            lineas.append(
                f"Distribucion: {detalle}"
            )

            lineas.append("-" * 55)

        escribir_resultados("\n".join(lineas))

        limpiar_tabla()

    # ==========================================
    # LIMPIAR RESULTADOS
    # ==========================================

    def limpiar_resultados():

        limpiar_tabla()
        selector.current(0)

        escribir_resultados(
            "Seleccione un monto y presione CALCULAR BILLETES."
        )

    # ==========================================
    # CONFIGURACION DE BOTONES
    # ==========================================

    tk.Button(
        botones,
        text="CALCULAR BILLETES",
        command=ejecutar_voraz,
        bg="#2563EB",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=15,
        pady=8
    ).pack(side="left", padx=(0, 10))

    tk.Button(
        botones,
        text="COMPARAR MONTOS",
        command=comparar_montos,
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

    ventana = iniciar_interfaz4(raiz)

    ventana.protocol(
        "WM_DELETE_WINDOW",
        raiz.destroy
    )

    raiz.mainloop()
