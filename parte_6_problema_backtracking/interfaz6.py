"""Interfaz gráfica para la Actividad 6 de Backtracking."""

import tkinter as tk
from tkinter import messagebox
import time

from parte_6_problema_backtracking.actividad6 import (formatear_ruta, generar_rutas_backtracking, respuesta_teorica)


ALMACENES = [
    "Lima",
    "Arequipa",
    "Cusco",
    "Trujillo",
    "Piura",
    "Chiclayo",
    "Ica",
    "Tacna",
]


class InterfazRutas:
    """Ventana principal del sistema de rutas."""

    def __init__(self, ventana: tk.Tk) -> None:
        self.ventana = ventana
        self.ventana.title("UPN Cargo - Rutas con Backtracking")
        self.ventana.geometry("900x600")
        self.ventana.configure(bg="#eaf2f8")

        self._crear_encabezado()
        self._crear_controles()
        self._crear_resultados()

    def _crear_encabezado(self) -> None:
        encabezado = tk.Frame(self.ventana, bg="#12355b", height=90)
        encabezado.pack(fill="x")

        tk.Label(
            encabezado,
            text="UPN CARGO S.A.C.",
            font=("Arial", 20, "bold"),
            fg="white",
            bg="#12355b",
        ).pack(anchor="w", padx=25, pady=(16, 0))

        tk.Label(
            encabezado,
            text="Actividad 6: generación de rutas con Backtracking",
            font=("Arial", 11),
            fg="#dbeafe",
            bg="#12355b",
        ).pack(anchor="w", padx=25, pady=(4, 12))

    def _crear_controles(self) -> None:
        panel = tk.LabelFrame(
            self.ventana,
            text="Configuración",
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#12355b",
            padx=12,
            pady=10,
        )
        panel.pack(side="left", fill="y", padx=20, pady=20)

        tk.Label(panel, text="Seleccione almacenes:", bg="white").pack(anchor="w")

        self.lista_almacenes = tk.Listbox(
            panel,
            selectmode=tk.MULTIPLE,
            height=10,
            width=22,
            font=("Arial", 10),
            exportselection=False,
        )
        self.lista_almacenes.pack(pady=8)

        for almacen in ALMACENES:
            self.lista_almacenes.insert(tk.END, almacen)
        self.lista_almacenes.selection_set(0, len(ALMACENES) - 1)

        tk.Label(panel, text="Almacén de origen:", bg="white").pack(anchor="w")

        self.origen = tk.StringVar(value="Lima")
        tk.OptionMenu(panel, self.origen, *ALMACENES).pack(fill="x", pady=(4, 12))

        tk.Label(panel, text="Máximo de rutas a mostrar:", bg="white").pack(anchor="w")

        self.limite = tk.Entry(panel, width=10)
        self.limite.insert(0, "10")
        self.limite.pack(anchor="w", pady=(4, 12))

        tk.Button(
            panel,
            text="GENERAR RUTAS",
            command=self.generar_rutas,
            bg="#1d70b8",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=8,
            pady=6,
        ).pack(fill="x", pady=4)

        tk.Button(
            panel,
            text="VER EXPLICACIÓN",
            command=self.mostrar_explicacion,
            bg="#5b8def",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=8,
            pady=6,
        ).pack(fill="x", pady=4)

    def _crear_resultados(self) -> None:
        panel = tk.LabelFrame(
            self.ventana,
            text="Resultados",
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#12355b",
            padx=10,
            pady=10,
        )
        panel.pack(side="right", fill="both", expand=True, padx=(0, 20), pady=20)

        self.estado = tk.Label(
            panel,
            text="Seleccione los almacenes y pulse GENERAR RUTAS.",
            bg="white",
            fg="#425466",
            anchor="w",
        )
        self.estado.pack(fill="x", pady=(0, 8))

        marco_salida = tk.Frame(panel, bg="white")
        marco_salida.pack(fill="both", expand=True)

        barra = tk.Scrollbar(marco_salida)
        barra.pack(side="right", fill="y")

        self.salida = tk.Text(
            marco_salida,
            wrap="word",
            font=("Consolas", 10),
            bg="#f8fbff",
            yscrollcommand=barra.set,
        )
        self.salida.pack(side="left", fill="both", expand=True)
        barra.config(command=self.salida.yview)

    def generar_rutas(self) -> None:
        indices = self.lista_almacenes.curselection()
        seleccionados = [ALMACENES[indice] for indice in indices]

        try:
            limite = int(self.limite.get())
            if limite < 1:
                raise ValueError
        except ValueError:
            messagebox.showerror("Dato incorrecto", "Escriba un número entero mayor que cero.")
            return

        origen = self.origen.get()
        if len(seleccionados) < 2:
            messagebox.showwarning("Selección insuficiente", "Seleccione por lo menos dos almacenes.")
            return

        if origen not in seleccionados:
            messagebox.showwarning("Origen incorrecto", "El origen debe estar seleccionado.")
            return

        rutas, estados = generar_rutas_backtracking(
            seleccionados,
            origen=origen,
            limite=limite,
        )

        self.salida.delete("1.0", tk.END)
        self.salida.insert(tk.END, "RUTAS ENCONTRADAS\n")
        self.salida.insert(tk.END, "=" * 70 + "\n")

        for numero, ruta in enumerate(rutas, start=1):
            self.salida.insert(tk.END, f"{numero:02d}. {formatear_ruta(ruta)}\n")

        self.estado.config(
            text=(
                f"Rutas mostradas: {len(rutas)} | Estados explorados: {estados} | "
                "Complejidad máxima: O(n!)"
            )
        )

    def mostrar_explicacion(self) -> None:
        self.salida.delete("1.0", tk.END)
        self.salida.insert(tk.END, "EXPLICACIÓN DEL BACKTRACKING\n")
        self.salida.insert(tk.END, "=" * 70 + "\n\n")

        for letra, texto in respuesta_teorica().items():
            self.salida.insert(tk.END, f"{letra}) {texto}\n\n")

        self.estado.config(text="Respuestas teóricas de la Actividad 6")


def iniciar_interfaz() -> None:
    ventana = tk.Tk()
    InterfazRutas(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    iniciar_interfaz()
