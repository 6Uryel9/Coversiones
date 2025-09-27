import time

def animacion_conversion(unidad1, unidad2):
    print("Convirtiendo", unidad1, "a", unidad2)
    for i in range(1, 11):  
        flecha = "=" * i + ">"
        print(flecha)
        time.sleep(0.2)  
    print("¡Conversión completada!")


def bytes_kilobytes():
    print("1. Bytes -> Kilobytes")
    print("2. Kilobytes -> Bytes")
    eleccion = int(input("Elige la conversión que quieres hacer: "))

    if eleccion == 1:
        valor = int(input("Ingresa el número de bytes: "))
        resultado = valor / 1024
        animacion_conversion("Bytes", "Kilobytes")
        print(valor, "bytes son igual a", resultado, "kilobytes")
        return resultado

    elif eleccion == 2:
        valor = int(input("Ingresa el número de kilobytes: "))
        resultado = valor * 1024
        animacion_conversion("Kilobytes", "Bytes")
        print(valor, "kilobytes son igual a", resultado, "bytes")
        return resultado

    else:
        print("Opción inválida")
        return None


def kilobytes_megabytes():
    print("1. Kilobytes -> Megabytes")
    print("2. Megabytes -> Kilobytes")
    eleccion = int(input("Elige la conversión que quieres hacer: "))

    if eleccion == 1:
        valor = int(input("Ingresa el número de kilobytes: "))
        resultado = valor / 1024
        animacion_conversion("Kilobytes", "Megabytes")
        print(valor, "kilobytes son igual a", resultado, "megabytes")
        return resultado

    elif eleccion == 2:
        valor = int(input("Ingresa el número de megabytes: "))
        resultado = valor * 1024
        animacion_conversion("Megabytes", "Kilobytes")
        print(valor, "megabytes son igual a", resultado, "kilobytes")
        return resultado

    else:
        print("Opción inválida")
        return None


def megabytes_gigabytes():
    print("1. Megabytes -> Gigabytes")
    print("2. Gigabytes -> Megabytes")
    eleccion = int(input("Elige la conversión que quieres hacer: "))

    if eleccion == 1:
        valor = int(input("Ingresa el número de megabytes: "))
        resultado = valor / 1024
        animacion_conversion("Megabytes", "Gigabytes")
        print(valor, "megabytes son igual a", resultado, "gigabytes")
        return resultado

    elif eleccion == 2:
        valor = float(input("Ingresa el número de gigabytes: "))
        resultado = valor * 1024
        animacion_conversion("Gigabytes", "Megabytes")
        print(valor, "gigabytes son igual a", resultado, "megabytes")
        return resultado

    else:
        print("Opción inválida")
        return None


def bps_megabps():
    print("1. bps -> Mbps")
    print("2. Mbps -> bps")
    eleccion = int(input("Elige la conversión que quieres hacer: "))

    if eleccion == 1:
        valor = float(input("Ingresa el número de bps: "))
        resultado = valor / 1_000_000
        animacion_conversion("bps", "Mbps")
        print(valor, "bps son igual a", resultado, "Mbps")
        return resultado

    elif eleccion == 2:
        valor = float(input("Ingresa el número de Mbps: "))
        resultado = valor * 1_000_000
        animacion_conversion("Mbps", "bps")
        print(valor, "Mbps son igual a", resultado, "bps")
        return resultado

    else:
        print("Opción inválida")
        return None


def pruebas_codigo():
    print("\n--- Iniciando pruebas automáticas ---")

    # Bytes <-> Kilobytes
    print("1024 Bytes ->", 1024 / 1024, "KB (esperado: 1)")
    print("1 KB ->", 1 * 1024, "Bytes (esperado: 1024)")

    # KB <-> MB
    print("2048 KB ->", 2048 / 1024, "MB (esperado: 2)")
    print("3 MB ->", 3 * 1024, "KB (esperado: 3072)")

    # MB <-> GB
    print("4096 MB ->", 4096 / 1024, "GB (esperado: 4)")
    print("5 GB ->", 5 * 1024, "MB (esperado: 5120)")

    # bps <-> Mbps
    print("1,000,000 bps ->", 1_000_000 / 1_000_000, "Mbps (esperado: 1)")
    print("2 Mbps ->", 2 * 1_000_000, "bps (esperado: 2000000)")

    print("--- Pruebas completadas ---\n")



def menu():
    print("\n--- Menú de conversiones digitales ---")
    print("1. Bytes ↔ Kilobytes")
    print("2. Kilobytes ↔ Megabytes")
    print("3. Megabytes ↔ Gigabytes")
    print("4. bits por segundo ↔ Megabits por segundo")
    print("5. Mostrar mensaje y regresar")
    print("6. Ejecutar pruebas automáticas")
    print("0. Salir")

    opcion = int(input("Ingrese la opción que requiera: "))
    return opcion

def main_calculadoradigital():
    while True:
        opcion = menu()

        if opcion == 1:
            resultado = bytes_kilobytes()

        elif opcion == 2:
            resultado = kilobytes_megabytes()

        elif opcion == 3:
            resultado = megabytes_gigabytes()

        elif opcion == 4:
            resultado = bps_megabps()

        elif opcion == 5:
            print("Regresando al menú principal...")
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="")
            print("\n")

        elif opcion == 6:
            pruebas_codigo()

        elif opcion == 0:
            print("Ha cerrado el programa")
            break

        else:
            print("Opción inválida, intente de nuevo.")


main_calculadoradigital()
