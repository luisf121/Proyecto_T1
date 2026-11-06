from parte_1_estructura_datos.actividad1 import pedidos


# ==========================================
# 1. ORDENAMIENTO BURBUJA
# ==========================================

def ordenamiento_burbuja(lista):

    pedidos_ordenados = lista.copy()
    cantidad_pedidos = len(pedidos_ordenados)

    if cantidad_pedidos <= 1:
        return pedidos_ordenados

    recorrido = 0

    while recorrido < cantidad_pedidos - 1:

        hubo_intercambio = False
        posicion = 0
        limite = cantidad_pedidos - recorrido - 1

        while posicion < limite:

            pedido_actual = pedidos_ordenados[posicion]
            pedido_siguiente = pedidos_ordenados[posicion + 1]

            costo_actual = pedido_actual["costo"]
            costo_siguiente = pedido_siguiente["costo"]

            if costo_actual > costo_siguiente:

                pedidos_ordenados[posicion] = pedido_siguiente
                pedidos_ordenados[posicion + 1] = pedido_actual

                hubo_intercambio = True

            posicion = posicion + 1

        if not hubo_intercambio:
            break

        recorrido = recorrido + 1

    return pedidos_ordenados


# ==========================================
# 2. ORDENAMIENTO POR SELECCIÓN
# ==========================================

def ordenamiento_seleccion(lista):

    pedidos_ordenados = lista.copy()
    cantidad_pedidos = len(pedidos_ordenados)

    if cantidad_pedidos <= 1:
        return pedidos_ordenados

    posicion_inicial = 0

    while posicion_inicial < cantidad_pedidos - 1:

        posicion_menor = posicion_inicial
        posicion_revision = posicion_inicial + 1

        while posicion_revision < cantidad_pedidos:

            pedido_revision = pedidos_ordenados[posicion_revision]
            pedido_menor = pedidos_ordenados[posicion_menor]

            costo_revision = pedido_revision["costo"]
            costo_menor = pedido_menor["costo"]

            if costo_revision < costo_menor:
                posicion_menor = posicion_revision

            posicion_revision = posicion_revision + 1

        if posicion_menor != posicion_inicial:

            pedido_temporal = pedidos_ordenados[posicion_inicial]
            pedido_seleccionado = pedidos_ordenados[posicion_menor]

            pedidos_ordenados[posicion_inicial] = pedido_seleccionado
            pedidos_ordenados[posicion_menor] = pedido_temporal

        posicion_inicial = posicion_inicial + 1

    return pedidos_ordenados


# ==========================================
# 3. ORDENAMIENTO POR INSERCIÓN
# ==========================================

def ordenamiento_insercion(lista):

    pedidos_ordenados = lista.copy()
    cantidad_pedidos = len(pedidos_ordenados)

    if cantidad_pedidos <= 1:
        return pedidos_ordenados

    posicion_actual = 1

    while posicion_actual < cantidad_pedidos:

        pedido_actual = pedidos_ordenados[posicion_actual]
        costo_actual = pedido_actual["costo"]

        posicion_anterior = posicion_actual - 1

        while posicion_anterior >= 0:

            pedido_anterior = pedidos_ordenados[posicion_anterior]
            costo_anterior = pedido_anterior["costo"]

            if costo_anterior > costo_actual:

                posicion_destino = posicion_anterior + 1

                pedidos_ordenados[posicion_destino] = pedido_anterior

                posicion_anterior = posicion_anterior - 1

            else:
                break

        posicion_insercion = posicion_anterior + 1

        pedidos_ordenados[posicion_insercion] = pedido_actual

        posicion_actual = posicion_actual + 1

    return pedidos_ordenados
