"""
Actividad 6 - Problema de Backtracking
UPN Cargo S.A.C.

Problema seleccionado: Generación de Permutaciones de Rutas.
El algoritmo genera todas las rutas posibles que visitan una vez cada almacén,
partiendo de un almacén de origen. Para limitar la demostración en la interfaz,
se permite trabajar con hasta ocho almacenes.
"""

from typing import List, Optional, Tuple


def generar_rutas_backtracking(
    almacenes: List[str],
    origen: Optional[str] = None,
    destino: Optional[str] = None,
    limite: Optional[int] = None,
) -> Tuple[List[List[str]], int]:
    """Genera rutas Hamiltonianas simples mediante Backtracking.

    Cada almacén aparece una sola vez. Si se indica origen, la ruta comienza allí.
    Si se indica destino, la ruta termina allí. El valor devuelto incluye las rutas
    encontradas y el número de estados explorados.
    """
    if not almacenes:
        return [], 0

    nombres = list(dict.fromkeys(almacenes))
    if origen is not None and origen not in nombres:
        raise ValueError("El almacén de origen no pertenece a la lista.")
    if destino is not None and destino not in nombres:
        raise ValueError("El almacén de destino no pertenece a la lista.")
    if origen is not None and destino is not None and origen == destino and len(nombres) > 1:
        raise ValueError("El origen y el destino deben ser diferentes.")

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
            if destino is not None and almacen == destino and len(ruta_actual) < len(nombres) - 1:
                continue

            # Elegir: se agrega un almacén a la ruta parcial.
            ruta_actual.append(almacen)
            visitados.add(almacen)

            # Explorar: se continúa con el siguiente almacén.
            backtracking()

            # Retroceder: se deshace la última elección para probar otra opción.
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
    """Convierte una ruta en un texto fácil de leer."""
    return " -> ".join(ruta)


def respuesta_teorica() -> dict:
    """Respuestas solicitadas por la Actividad 6."""
    return {
        "a": (
            "El algoritmo construye una ruta parcial agregando un almacén no visitado. "
            "Después explora recursivamente las alternativas restantes hasta completar "
            "la ruta o detectar que la configuración no es válida."
        ),
        "b": (
            "El algoritmo retrocede cuando una ruta parcial no puede conducir a una "
            "solución válida o cuando ya terminó de explorar una alternativa. "
            "El último almacén elegido se elimina y se prueba otra opción."
        ),
        "c": (
            "Backtracking evita continuar por ramas que ya no pueden producir una "
            "solución válida. Esto reduce la exploración frente a una búsqueda exhaustiva "
            "que revisaría todas las configuraciones sin poda."
        ),
        "d": (
            "Su principal desventaja es el crecimiento factorial del número de rutas. "
            "Con ocho almacenes puede haber hasta 8! configuraciones, por lo que el "
            "tiempo de ejecución aumenta rápidamente. También requiere memoria para la "
            "recursión y el control de las rutas parciales."
        ),
    }


if __name__ == "__main__":
    almacenes = ["Lima", "Arequipa", "Cusco", "Trujillo", "Piura", "Chiclayo", "Ica", "Tacna"]
    rutas, estados = generar_rutas_backtracking(
        almacenes,
        origen="Lima",
        limite=10,
    )

    print("ACTIVIDAD 6 - GENERACIÓN DE PERMUTACIONES DE RUTAS")
    print(f"Rutas mostradas: {len(rutas)}")
    print(f"Estados explorados: {estados}\n")
    for numero, ruta in enumerate(rutas, start=1):
        print(f"{numero:02d}. {formatear_ruta(ruta)}")
