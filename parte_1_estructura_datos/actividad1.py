
# ACTIVIDAD 1: ESTRUCTURAS DE DATOS


# Registro de pedidos mediante diccionarios
# Almacenados dentro de una lista

pedidos = [
    {"codigo": "P001", "cliente": "Juan Perez", "ciudad": "Lima", "peso": 5.5, "prioridad": "Alta", "costo": 35.00},
    {"codigo": "P002", "cliente": "Maria Torres", "ciudad": "Arequipa", "peso": 8.0, "prioridad": "Media", "costo": 50.00},
    {"codigo": "P003", "cliente": "Carlos Ramirez", "ciudad": "Cusco", "peso": 3.2, "prioridad": "Baja", "costo": 28.00},
    {"codigo": "P004", "cliente": "Ana Garcia", "ciudad": "Ica", "peso": 6.0, "prioridad": "Alta", "costo": 40.00},
    {"codigo": "P005", "cliente": "Luis Fernandez", "ciudad": "Piura", "peso": 10.5, "prioridad": "Media", "costo": 65.00},
    {"codigo": "P006", "cliente": "Rosa Mendoza", "ciudad": "Trujillo", "peso": 4.0, "prioridad": "Baja", "costo": 32.00},
    {"codigo": "P007", "cliente": "Pedro Castillo", "ciudad": "Lima", "peso": 7.5, "prioridad": "Alta", "costo": 45.00},
    {"codigo": "P008", "cliente": "Lucia Ramirez", "ciudad": "Chiclayo", "peso": 2.5, "prioridad": "Media", "costo": 25.00},
    {"codigo": "P009", "cliente": "Miguel Torres", "ciudad": "Huancayo", "peso": 9.0, "prioridad": "Baja", "costo": 55.00},
    {"codigo": "P010", "cliente": "Elena Vargas", "ciudad": "Tacna", "peso": 5.0, "prioridad": "Alta", "costo": 38.00},
    {"codigo": "P011", "cliente": "Jorge Mendoza", "ciudad": "Puno", "peso": 6.5, "prioridad": "Media", "costo": 42.00},
    {"codigo": "P012", "cliente": "Carmen Flores", "ciudad": "Iquitos", "peso": 12.0, "prioridad": "Baja", "costo": 75.00},
    {"codigo": "P013", "cliente": "Daniel Perez", "ciudad": "Lima", "peso": 3.5, "prioridad": "Alta", "costo": 30.00},
    {"codigo": "P014", "cliente": "Patricia Gomez", "ciudad": "Ayacucho", "peso": 8.5, "prioridad": "Media", "costo": 52.00},
    {"codigo": "P015", "cliente": "Roberto Sanchez", "ciudad": "Cajamarca", "peso": 4.5, "prioridad": "Baja", "costo": 36.00}
]



# FUNCION DE BUSQUEDA POR CLIENTE


def buscar_por_cliente(pedidos, nombre_buscar):

    resultados = []

    for pedido in pedidos:

        if nombre_buscar.lower() in pedido["cliente"].lower():
            resultados.append(pedido)

    return resultados
