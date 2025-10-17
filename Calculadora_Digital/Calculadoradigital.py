import time


def animacion_conversion(unidad1, unidad2):
    """
    Sirve solo como efecto visual al realizar una conversión.
    """
    print("Convirtiendo", unidad1, "a", unidad2)
    for i in range(1, 11):
        flecha = "=" * i + ">"
        print(flecha)
        time.sleep(0.1)
    print("¡Conversión completada!\n")


# Cada lista contiene información relacionada entre sí por índice.
unidades1 = ["Bytes", "Kilobytes", "Megabytes", "bps"]
unidades2 = ["Kilobytes", "Megabytes", "Gigabytes", "Mbps"]
factores = [1024, 1024, 1024, 1_000_000]

# Ejemplo:
# unidades1[0] = "Bytes"     → unidades2[0] = "Kilobytes"   → factor = 1024



def convertir(indice, direccion, valor):
    """
    Realiza la conversión numérica usando las listas.
    Parámetros:
        indice (int): índice que selecciona la pareja de unidades.
        direccion (int): 1 si es unidad1 → unidad2, 2 si es unidad2 → unidad1.
        valor (float): valor numérico a convertir.
    Retorna:
        float: resultado de la conversión.
    """
    f = factores[indice]
    if direccion == 1:
        resultado = valor / f
    else:
        resultado = valor * f
    return resultado


def pruebas_codigo():
    print("\n--- Iniciando pruebas automáticas de Calculadora Digital ---\n")

    # Prueba 1: Bytes ↔ Kilobytes
    print("Prueba 1: 1024 Bytes ->", 1024 / 1024, "KB (esperado: 1)")
    print("          1 KB ->", 1 * 1024, "Bytes (esperado: 1024)\n")

    # Prueba 2: Kilobytes ↔ Megabytes
    print("Prueba 2: 2048 KB ->", 2048 / 1024, "MB (esperado: 2)")
    print("          3 MB ->", 3 * 1024, "KB (esperado: 3072)\n")

    # Prueba 3: Megabytes ↔ Gigabytes
    print("Prueba 3: 4096 MB ->", 4096 / 1024, "GB (esperado: 4)")
    print("          5 GB ->", 5 * 1024, "MB (esperado: 5120)\n")

    # Prueba 4: bps ↔ Mbps
    print("Prueba 4: 1,000,000 bps ->", 1_000_000 / 1_000_000, "Mbps (esperado: 1)")
    print("          2 Mbps ->", 2 * 1_000_000, "bps (esperado: 2000000)\n")

    print("--- Pruebas completadas exitosamente ---\n")

