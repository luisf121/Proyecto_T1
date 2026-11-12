"""Interfaz gráfica para la Actividad 6 de Backtracking."""

import tkinter as tk
from tkinter import messagebox

try:
    from .actividad6 import (
        formatear_ruta,
        generar_rutas_backtracking,
        respuesta_teorica,
    )
except ImportError:
    from actividad6 import (
        formatear_ruta,
        generar_rutas_backtracking,
        respuesta_teorica,
    )


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

        self.ventana.title(
            "UPN Cargo - Actividad 6"
        )
        self.ventana.geometry(
            "900x600"
        )
        self.ventana.minsize(
            800,
            500
        )
        self.ventana.configure(
            bg="#eaf2f8"
        )

        self._crear_encabezado()
        self._crear_controles()
        self._crear_resultados()

    def _crear_encabezado(self) -> None:
        encabezado = tk.Frame(
            self.ventana,
            bg="#12355b",
            height=95
        )
        encabezado.pack(
            fill="x"
        )
        encabezado.pack_propagate(
            False
        )

        tk.Label(
            encabezado,
            text="UPN CARGO S.A.C. | PARTE 6",
            font=("Arial", 20, "bold"),
            fg="white",
            bg="#12355b"
        ).pack(
            anchor="w",
            padx=25,
            pady=(16, 0)
        )

        tk.Label(
            encabezado,
            text=(
                "Generación de permutaciones de rutas "
                "con Backtracking"
            ),
            font=("Arial", 11),
            fg="#dbeafe",
            bg="#12355b"
        ).pack(
            anchor="w",
            padx=25,
            pady=(4, 12)
        )

    def _crear_controles(self) -> None:
        panel = tk.LabelFrame(
            self.ventana,
            text="Configuración",
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#12355b",
            padx=12,
            pady=10
        )
        panel.pack(
            side="left",
            fill="y",
            padx=20,
            pady=20
        )

        tk.Label(
            panel,
            text="Seleccione los almacenes:",
            bg="white",
            font=("Arial", 10)
        ).pack(
            anchor="w"
        )

        self.lista_almacenes = tk.Listbox(
            panel,
            selectmode=tk.MULTIPLE,
            height=10,
            width=22,
            font=("Arial", 10),
            exportselection=False,
            selectbackground="#1d70b8",
            selectforeground="white"
        )
        self.lista_almacenes.pack(
            pady=8
        )

        for almacen in ALMACENES:
            self.lista_almacenes.insert(
                tk.END,
                almacen
            )

        self.lista_almacenes.selection_set(
            0,
            len(ALMACENES) - 1
        )

        tk.Label(
            panel,
            text="Almacén de origen:",
            bg="white",
            font=("Arial", 10)
        ).pack(
            anchor="w"
        )

        self.origen = tk.StringVar(
            value="Lima"
        )

        menu_origen = tk.OptionMenu(
            panel,
            self.origen,
            *ALMACENES
        )
        menu_origen.config(
            width=18,
            bg="#f4f7fb",
            font=("Arial", 10)
        )
        menu_origen.pack(
            fill="x",
            pady=(4, 12)
        )

        tk.Label(
            panel,
            text="Máximo de rutas a mostrar:",
            bg="white",
            font=("Arial", 10)
        ).pack(
            anchor="w"
        )

        self.limite = tk.Entry(
            panel,
            width=10,
            font=("Arial", 10)
        )
        self.limite.insert(
            0,
            "10"
        )
        self.limite.pack(
            anchor="w",
            pady=(4, 12)
        )

        tk.Button(
            panel,
            text="GENERAR RUTAS",
            command=self.generar_rutas,
            bg="#1d70b8",
            fg="white",
            activebackground="#155a91",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            padx=8,
            pady=7,
            relief="flat",
            cursor="hand2"
        ).pack(
            fill="x",
            pady=4
        )

        tk.Button(
            panel,
            text="VER EXPLICACIÓN",
            command=self.mostrar_explicacion,
            bg="#5b8def",
            fg="white",
            activebackground="#426fc9",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            padx=8,
            pady=7,
            relief="flat",
            cursor="hand2"
        ).pack(
            fill="x",
            pady=4
        )

        tk.Button(
            panel,
            text="LIMPIAR RESULTADOS",
            command=self.limpiar_resultados,
            bg="#64748b",
            fg="white",
            activebackground="#475569",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            padx=8,
            pady=7,
            relief="flat",
            cursor="hand2"
        ).pack(
            fill="x",
            pady=4
        )

    def _crear_resultados(self) -> None:
        panel = tk.LabelFrame(
            self.ventana,
            text="Resultados del algoritmo",
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#12355b",
            padx=10,
            pady=10
        )
        panel.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(0, 20),
            pady=20
        )

        self.estado = tk.Label(
            panel,
            text=(
                "Seleccione los almacenes. Cada ruta "
                "visitará cada almacén una sola vez."
            ),
            bg="white",
            fg="#425466",
            anchor="w",
            justify="left",
            font=("Arial", 10)
        )
        self.estado.pack(
            fill="x",
            pady=(0, 8)
        )

        marco_salida = tk.Frame(
            panel,
            bg="white"
        )
        marco_salida.pack(
            fill="both",
            expand=True
        )

        barra = tk.Scrollbar(
            marco_salida
        )
        barra.pack(
            side="right",
            fill="y"
        )

        self.salida = tk.Text(
            marco_salida,
            wrap="word",
            font=("Consolas", 10),
            bg="#f8fbff",
            fg="#1f2933",
            padx=10,
            pady=10,
            yscrollcommand=barra.set,
            relief="solid",
            borderwidth=1
        )
        self.salida.pack(
            side="left",
            fill="both",
            expand=True
        )

        barra.config(
            command=self.salida.yview
        )

    def generar_rutas(self) -> None:
        indices = self.lista_almacenes.curselection()

        seleccionados = [
            ALMACENES[indice]
            for indice in indices
        ]

        try:
            limite = int(
                self.limite.get()
            )

            if limite < 1:
                raise ValueError

        except (TypeError, ValueError):
            messagebox.showerror(
                "Dato incorrecto",
                "Escriba un número entero mayor que cero."
            )
            return

        origen = self.origen.get()

        if len(seleccionados) < 2:
            messagebox.showwarning(
                "Selección insuficiente",
                "Seleccione por lo menos dos almacenes."
            )
            return

        if origen not in seleccionados:
            messagebox.showwarning(
                "Origen incorrecto",
                "El almacén de origen debe estar seleccionado."
            )
            return

        try:
            rutas, estados = generar_rutas_backtracking(
                seleccionados,
                origen=origen,
                limite=limite
            )

        except ValueError as error:
            messagebox.showerror(
                "Error al generar rutas",
                str(error)
            )
            return

        self.salida.delete(
            "1.0",
            tk.END
        )

        self.salida.insert(
            tk.END,
            "ACTIVIDAD 6 - RUTAS GENERADAS\n"
        )
        self.salida.insert(
            tk.END,
            "=" * 75 + "\n\n"
        )

        self.salida.insert(
            tk.END,
            f"Almacén de origen: {origen}\n"
        )
        self.salida.insert(
            tk.END,
            f"Almacenes seleccionados: {len(seleccionados)}\n"
        )
        self.salida.insert(
            tk.END,
            f"Máximo de rutas: {limite}\n\n"
        )

        self.salida.insert(
            tk.END,
            "RUTAS ENCONTRADAS\n"
        )
        self.salida.insert(
            tk.END,
            "-" * 75 + "\n"
        )

        if rutas:
            for numero, ruta in enumerate(
                rutas,
                start=1
            ):
                self.salida.insert(
                    tk.END,
                    f"{numero:02d}. "
                    f"{formatear_ruta(ruta)}\n"
                )
        else:
            self.salida.insert(
                tk.END,
                "No se encontraron rutas.\n"
            )

        self.estado.config(
            text=(
                f"Rutas mostradas: {len(rutas)} | "
                f"Estados explorados: {estados} | "
                "Complejidad máxima: O(n!)"
            )
        )

    def mostrar_explicacion(self) -> None:
        self.salida.delete(
            "1.0",
            tk.END
        )

        self.salida.insert(
            tk.END,
            "EXPLICACIÓN DEL BACKTRACKING\n"
        )
        self.salida.insert(
            tk.END,
            "=" * 75 + "\n\n"
        )

        for letra, texto in respuesta_teorica().items():
            self.salida.insert(
                tk.END,
                f"{letra}) {texto}\n\n"
            )

        self.estado.config(
            text="Respuestas teóricas de la Actividad 6."
        )

    def limpiar_resultados(self) -> None:
        self.salida.delete(
            "1.0",
            tk.END
        )

        self.estado.config(
            text=(
                "Seleccione los almacenes. Cada ruta "
                "visitará cada almacén una sola vez."
            )
        )


def iniciar_interfaz6(ventana_padre=None) -> None:
    """Inicia la ventana gráfica de la Actividad 6."""

    if ventana_padre is None:
        ventana = tk.Tk()
        ejecutar_bucle = True
    else:
        ventana = tk.Toplevel(
            ventana_padre
        )
        ejecutar_bucle = False

    InterfazRutas(
        ventana
    )

    if ejecutar_bucle:
        ventana.mainloop()


def iniciar_interfaz() -> None:
    """Alias de compatibilidad."""

    iniciar_interfaz6()


if __name__ == "__main__":
    iniciar_interfaz6()
