
# ALGORITMOS DE BUSQUEDA

# Importamos los pedidos de la Actividad 1

from parte_1_estructura_datos.actividad1 import pedidos


# ==========================================
# 1. BUSQUEDA LINEAL
# ==========================================

def busqueda_lineal(lista, codigo):

    for i in range(len(lista)):

        if lista[i]["codigo"] == codigo:
            return lista[i]

    return None



# 2. BUSQUEDA LINEAL ACOTADA


def busqueda_lineal_acotada(lista, codigo, limite):

    limite = min(limite, len(lista))

    for i in range(limite):

        if lista[i]["codigo"] == codigo:
            return lista[i]

    return None



# 3. BUSQUEDA BINARIA ITERATIVA


def busqueda_binaria_iterativa(lista, codigo):

    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:

        medio = (izquierda + derecha) // 2

        codigo_actual = lista[medio]["codigo"]

        if codigo_actual == codigo:
            return lista[medio]

        elif codigo_actual < codigo:
            izquierda = medio + 1

        else:
            derecha = medio - 1

    return None



# 4. BUSQUEDA BINARIA RECURSIVA


def busqueda_binaria_recursiva(lista, codigo, izquierda=0, derecha=None):

    if derecha is None:
        derecha = len(lista) - 1

    if izquierda > derecha:
        return None

    medio = (izquierda + derecha) // 2

    codigo_actual = lista[medio]["codigo"]

    if codigo_actual == codigo:
        return lista[medio]

    elif codigo_actual < codigo:
        return busqueda_binaria_recursiva(
            lista, codigo, medio + 1, derecha
        )

    else:
        return busqueda_binaria_recursiva(
            lista, codigo, izquierda, medio - 1
        )



# LISTA ORDENADA PARA BUSQUEDA BINARIA


pedidos_ordenados = sorted(
    pedidos,
    key=lambda pedido: pedido["codigo"]
)
