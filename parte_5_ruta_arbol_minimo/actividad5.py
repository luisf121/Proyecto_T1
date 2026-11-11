
# ACTIVIDAD 5 - RUTA DE ENTREGA Y ARBOL DE RECUBRIMIENTO MINIMO
# Empresa: UPN Cargo S.A.C.


CIUDADES = [
    "Lima",
    "Arequipa",
    "Cusco",
    "Trujillo",
    "Piura",
    "Chiclayo"
]


# Conexiones entre centros de distribucion
# (origen, destino, costo)

# El costo de cada tramo es la distancia recorrida en kilometros.
# Se usa como medida del costo logistico del envio.

CONEXIONES = [
    ("Lima", "Trujillo", 560),
    ("Lima", "Chiclayo", 770),
    ("Lima", "Piura", 980),
    ("Lima", "Arequipa", 1010),
    ("Lima", "Cusco", 1100),
    ("Trujillo", "Chiclayo", 210),
    ("Trujillo", "Piura", 420),
    ("Chiclayo", "Piura", 210),
    ("Arequipa", "Cusco", 510)
]


# ==========================================
# CONSTRUCCION DEL GRAFO
# ==========================================

# El grafo se guarda como un diccionario de diccionarios.
# Cada ciudad apunta a sus vecinos con el costo del tramo.
#
# Ejemplo: grafo["Lima"]["Trujillo"] = 560
#
# Se carga como grafo no dirigido: cada conexion se registra
# en los dos sentidos porque el tramo se puede recorrer en ambos.

def construir_grafo(conexiones=None):

    if conexiones is None:
        conexiones = CONEXIONES

    grafo = {}

    # Primero se crean todas las ciudades, aunque no tengan conexiones,
    # para que el grafo siempre tenga los seis centros de distribucion.
    for ciudad in CIUDADES:
        grafo[ciudad] = {}

    for origen, destino, costo in conexiones:

        if origen not in grafo:
            grafo[origen] = {}

        if destino not in grafo:
            grafo[destino] = {}

        grafo[origen][destino] = costo
        grafo[destino][origen] = costo

    return grafo


# ==========================================
# 1. RUTA ENTRE DOS CIUDADES (DIJKSTRA)
# ==========================================

# Busca la ruta de menor costo entre dos ciudades.
# En cada paso visita la ciudad pendiente con menor costo acumulado.
#
# Complejidad: O(n^2), donde n es la cantidad de ciudades.
# Se busca el minimo recorriendo la lista, sin usar heapq,
# para mantener el mismo estilo del resto del proyecto.

def ruta_mas_corta(grafo, origen, destino):

    if origen not in grafo or destino not in grafo:
        return None, None

    if origen == destino:
        return [origen], 0

    # distancias guarda el menor costo conocido desde el origen.
    # anteriores guarda de que ciudad se llego a cada ciudad.
    distancias = {}
    anteriores = {}
    visitados = set()

    for ciudad in grafo:
        distancias[ciudad] = float("inf")
        anteriores[ciudad] = None

    distancias[origen] = 0

    while len(visitados) < len(grafo):

        # 1. Se elige la ciudad pendiente con menor costo acumulado.
        ciudad_actual = None
        menor_costo = float("inf")

        for ciudad in grafo:

            if ciudad in visitados:
                continue

            if distancias[ciudad] < menor_costo:
                menor_costo = distancias[ciudad]
                ciudad_actual = ciudad

        if ciudad_actual is None:
            break

        # 2. Si ya se llego al destino no hace falta seguir explorando.
        if ciudad_actual == destino:
            break

        visitados.add(ciudad_actual)

        # 3. Se actualizan los vecinos con el costo acumulado.
        for vecino, costo in grafo[ciudad_actual].items():

            if vecino in visitados:
                continue

            costo_nuevo = distancias[ciudad_actual] + costo

            if costo_nuevo < distancias[vecino]:

                distancias[vecino] = costo_nuevo
                anteriores[vecino] = ciudad_actual

    # Si el destino quedo en infinito, no hay ruta entre las ciudades.
    if distancias[destino] == float("inf"):
        return None, None

    # 4. Se reconstruye el camino desde el destino hacia el origen.
    camino = []
    ciudad = destino

    while ciudad is not None:
        camino.append(ciudad)
        ciudad = anteriores[ciudad]

    camino.reverse()

    return camino, distancias[destino]


# ==========================================
# 2. ARBOL DE RECUBRIMIENTO MINIMO (PRIM)
# ==========================================

# Parte de una ciudad y en cada paso agrega el tramo mas barato
# que une una ciudad del arbol con una ciudad que aun no pertenece.
#
# El resultado siempre tiene (cantidad de ciudades - 1) tramos
# y conecta todas las ciudades con el menor costo total posible.
#
# Complejidad: O(n^3) con esta implementacion sencilla, porque
# por cada tramo se revisan todos los tramos disponibles.

def arbol_recubrimiento_minimo(grafo, inicio="Lima"):

    if inicio not in grafo:
        return [], 0

    en_arbol = {inicio}
    aristas = []

    while len(en_arbol) < len(grafo):

        # 1. Se busca el tramo mas barato que salga del arbol actual.
        mejor_arista = None

        for ciudad in en_arbol:

            for vecino, costo in grafo[ciudad].items():

                # Los tramos internos del arbol no sirven: formarian un ciclo.
                if vecino in en_arbol:
                    continue

                if mejor_arista is None or costo < mejor_arista[2]:
                    mejor_arista = (ciudad, vecino, costo)

        # Si no hay tramos hacia afuera, el grafo no es conexo.
        if mejor_arista is None:
            break

        # 2. Se agrega el tramo elegido y la ciudad nueva al arbol.
        aristas.append(mejor_arista)
        en_arbol.add(mejor_arista[1])

    costo_total = sum(costo for _, _, costo in aristas)

    return aristas, costo_total


# ==========================================
# EJECUCION INDEPENDIENTE
# ==========================================

if __name__ == "__main__":

    grafo = construir_grafo()

    print("UPN CARGO S.A.C.")
    print("ACTIVIDAD 5 - RUTA DE ENTREGA Y ARBOL DE RECUBRIMIENTO MINIMO")

    camino, costo = ruta_mas_corta(grafo, "Piura", "Cusco")

    print("\nRuta mas corta Piura -> Cusco")
    print(" -> ".join(camino))
    print(f"Costo total: {costo}")

    aristas, costo_total = arbol_recubrimiento_minimo(grafo)

    print("\nArbol de recubrimiento minimo")

    for origen, destino, costo_tramo in aristas:
        print(f"{origen} - {destino}: {costo_tramo}")

    print(f"Costo total: {costo_total}")
