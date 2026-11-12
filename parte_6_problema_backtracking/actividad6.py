"""
Parte 6 - Problema de Backtracking
La empresa debe distribuir productos en ocho almacenes.
El algoritmo genera rutas en las que cada almacén se visita
una sola vez, comenzando desde un almacén de origen.
"""

from typing import List, Optional, Tuple


def generar_rutas_backtracking(
    almacenes: List[str],
    origen: Optional[str] = None,
    destino: Optional[str] = None,
    limite: Optional[int] = None,
) -> Tuple[List[List[str]], int]:
    """
    Genera rutas mediante el algoritmo de Backtracking.

    Cada almacén aparece una sola vez en cada ruta.
    La ruta puede comenzar en un origen y terminar en un destino.
    """

    if not almacenes:
        return [], 0

    nombres = list(dict.fromkeys(almacenes))

    if origen is not None and origen not in nombres:
        raise ValueError(
            "El almacén de origen no pertenece a la lista."
        )

    if destino is not None and destino not in nombres:
        raise ValueError(
            "El almacén de destino no pertenece a la lista."
        )

    if (
        origen is not None
        and destino is not None
        and origen == destino
        and len(nombres) > 1
    ):
        raise ValueError(
            "El origen y el destino deben ser diferentes."
        )

    if limite is not None and limite < 1:
        raise ValueError(
            "El límite debe ser mayor que cero."
        )

    rutas: List[List[str]] = []
    ruta_actual: List[str] = []
    visitados = set()
    estados_explorados = 0

    def backtracking() -> None:
        nonlocal estados_explorados

        estados_explorados += 1

        if limite is not None and len(rutas) >= limite:
            return

        if len(ruta_actual) == len(nombres):
            if destino is None or ruta_actual[-1] == destino:
                rutas.append(ruta_actual.copy())

            return

        for almacen in nombres:

            if almacen in visitados:
                continue

            # El destino solo puede ser el último almacén.
            if (
                destino is not None
                and almacen == destino
                and len(ruta_actual) < len(nombres) - 1
            ):
                continue

            # Elegir
            ruta_actual.append(almacen)
            visitados.add(almacen)

            # Explorar
            backtracking()

            # Retroceder
            visitados.remove(almacen)
            ruta_actual.pop()

            if limite is not None and len(rutas) >= limite:
                return

    if origen is not None:
        ruta_actual.append(origen)
        visitados.add(origen)
        backtracking()
    else:
        backtracking()

    return rutas, estados_explorados


def formatear_ruta(ruta: List[str]) -> str:
    """
    Convierte una lista de almacenes en una ruta legible.
    """

    return " -> ".join(ruta)


def respuesta_teorica() -> dict:
    """
    Devuelve las respuestas teóricas de la Actividad 6.
    """

    return {
        "a": (
            "El algoritmo construye una ruta parcial agregando un "
            "almacén que todavía no ha sido visitado. Luego continúa "
            "explorando recursivamente las alternativas restantes "
            "hasta completar la ruta."
        ),

        "b": (
            "El algoritmo retrocede cuando termina de explorar una "
            "alternativa o cuando la ruta parcial ya no puede producir "
            "una solución válida. Para ello elimina el último almacén "
            "agregado y prueba otra opción."
        ),

        "c": (
            "Backtracking permite explorar las diferentes rutas y "
            "retroceder para probar nuevas alternativas. También evita "
            "continuar utilizando almacenes que ya fueron visitados."
        ),

        "d": (
            "La principal desventaja es su crecimiento factorial. "
            "Con ocho almacenes pueden existir hasta 8! configuraciones. "
            "Por esa razón, el tiempo de ejecución aumenta cuando se "
            "incrementa la cantidad de almacenes."
        ),
    }


if __name__ == "__main__":

    almacenes = [
        "Lima",
        "Arequipa",
        "Cusco",
        "Trujillo",
        "Piura",
        "Chiclayo",
        "Ica",
        "Tacna",
    ]

    rutas, estados = generar_rutas_backtracking(
        almacenes,
        origen="Lima",
        limite=10,
    )

    print("PARTE 6 - PROBLEMA DE BACKTRACKING")
    print("UPN CARGO S.A.C.")
    print()
    print("Problema seleccionado:")
    print("Generación de Permutaciones de Rutas")
    print()
    print(f"Rutas mostradas: {len(rutas)}")
    print(f"Estados explorados: {estados}")
    print()

    print("RUTAS GENERADAS")
    print("=" * 70)

    for numero, ruta in enumerate(rutas, start=1):
        print(
            f"{numero:02d}. {formatear_ruta(ruta)}"
        )

    print()
    print("RESPUESTAS TEÓRICAS")
    print("=" * 70)

    for letra, respuesta in respuesta_teorica().items():
        print(f"{letra}) {respuesta}")
        print()
