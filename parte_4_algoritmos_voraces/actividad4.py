
# ACTIVIDAD 4 - ALGORITMOS VORACES
# Empresa: UPN Cargo S.A.C.

BILLETES = [200, 100, 50, 20, 10]
MONTOS = [380, 670, 920]


def calcular_billetes(monto):
    resultado = {}
    restante = monto

    for billete in BILLETES:
        cantidad = restante // billete

        if cantidad > 0:
            resultado[billete] = cantidad
            restante = restante % billete

    return resultado, restante


def mostrar_resultados():
    print("UPN CARGO S.A.C.")
    print("ACTIVIDAD 4 - ALGORITMOS VORACES")

    for monto in MONTOS:
        resultado, restante = calcular_billetes(monto)

        print(f"\nMonto solicitado: S/ {monto}")

        for billete, cantidad in resultado.items():
            print(f"Billetes de S/ {billete}: {cantidad}")

        print(f"Total de billetes: {sum(resultado.values())}")
        print(f"Monto restante: S/ {restante}")


if __name__ == "__main__":
    mostrar_resultados()
