import time

unidades1 = ["Bytes", "Kilobytes", "Megabytes", "bps"]
unidades2 = ["Kilobytes", "Megabytes", "Gigabytes", "Mbps"]
factores = [1024, 1024, 1024, 1000000]


def animacion_conversion(unidad1, unidad2):
    """
    Muestra una animación mientras se realiza la conversión.
    """
    print(f"\nConvirtiendo {unidad1} a {unidad2}...")
    for i in range(1, 11):
        print("=" * i + ">")
        time.sleep(0.1)
    print("¡Conversión completada!\n")


def convertir(indice, direccion, valor):
    """
    Realiza la conversión entre unidades usando listas y condicionales anidadas.
    Parámetros:
        indice (int): selecciona el tipo de conversión
        direccion (int): selecciona la dirección de la conversión
        valor (float): aquí se ingresa el valor
    """
    if indice < 0 or indice >= len(factores):
        print("El índice no cuadra con las opciones")
        return None
    else:
        if valor == 0:
            print("Estás eligiendo cero a multiplicar.")
        elif valor < 0:
            print("Estás multiplicando con negativos.")
        else:
            print("Sigueindo la conversión...")

            f = factores[indice]

            if direccion == 1:
                if f == 1024:
                    resultado = valor / f
                elif f == 1000000:
                    resultado = valor / f
                else:
                    resultado = valor / f
            elif direccion == 2:
                if f == 1024:
                    resultado = valor * f
                elif f == 1000000:
                    resultado = valor * f
                else:
                    resultado = valor * f
            else:
                print("Escribe 1 o 2 para la dirección, porfa.")
                return None

            if resultado == 0:
                print("Tu resultado es cero, mejor ingresa otros datos, amigo")
            else:
                print("Conversión bien ejecutada...")

            return resultado

def tabla_conversiones():
    """
    Muestra una matriz con conversiones tomadas del archivo historial.txt.
    Cada línea del historial debe tener el formato: "Unidad1 ↔ Unidad2: valor -> resultado"
    """
    print("\n--- Tabla de conversiones recientes ---")

    matriz = [["Unidad 1", "Unidad 2", "Valor base", "Resultado"]]

    try:
        with open("historial.txt", "r", encoding="utf-8") as f:
            lineas = f.readlines()

        for linea in lineas:
            partes = linea.strip().split(":")
            if len(partes) == 2:
                cabecera = partes[0].strip()
                cuerpo = partes[1].strip()
                unidades = cabecera.replace("↔", "").split()
                valores = cuerpo.split("->")

                if len(unidades) >= 2 and len(valores) == 2:
                    unidad1 = unidades[0]
                    unidad2 = unidades[-1]
                    valor = valores[0].strip()
                    resultado = valores[1].strip()
                    fila = [unidad1, unidad2, valor, resultado]
                    matriz.append(fila)

        for fila in matriz:
            print(fila)

        print("\nFin de la tabla.\n")

    except FileNotFoundError:
        print("Aún no hay conversiones registradas, ingeniero.\n")


def confirmacion():
    """
    Solicita confirmación al usuario antes de continuar.
    """
    respuesta = input("¿Estás seguro de continuar con la conversión? (s/n): ")
    while respuesta.lower() not in ("s", "n"):
        respuesta = input("Por favor escribe 's' o 'n': ")

    if respuesta.lower() == "s":
        print("¡Confirmado! Procediendo...\n")
        return True
    else:
        print("No se confirmó.\n")
        return False


def verificar_unidad(unidad):
    """
    Devuelve True si la unidad existe en unidades1 o unidades2; False en caso contrario.
    """
    if unidad in unidades1:
        print(f"La unidad {unidad} pertenece a unidades1.")
        return True
    elif unidad in unidades2:
        print(f"La unidad {unidad} pertenece a unidades2.")
        return True
    else:
        print("Unidad no reconocida.")
        return False


def mostrar_tipo_conversion(indice):
    """
    Muestra una descripción del tipo de conversión según el índice.
    """
    if indice == 0:
        print("Conversión de Bytes a Kilobytes")
    elif indice == 1:
        print("Conversión de Kilobytes a Megabytes")
    elif indice == 2:
        print("Conversión de Megabytes a Gigabytes")
    elif indice == 3:
        print("Conversión de bps a Mbps")
    else:
        print("Índice fuera de rango, conversión no reconocida.")


def pedir_valor():
    """
    Solicita un valor numérico al usuario y valida que sea correcto (no negativo).
    """
    while True:
        try:
            valor = float(input("Introduce el valor a convertir: "))
            if valor < 0:
                print("No se permiten valores negativos.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Debes escribir un número.")



def guardar_en_archivo(texto):
    """
    Agrega una línea al archivo historial.txt.
    """
    with open("historial.txt", "a", encoding="utf-8") as f:
        f.write(texto + "\n")


def pruebas_codigo():
    """
    Muestra tabla con las pruebas automáticas.
    """
    print("\n--- Pruebas automáticas de Calculadora Digital ---")

    matriz = [["Unidad 1", "Unidad 2", "Valor base", "Resultado"]]
    valores_prueba = [1024, 2048, 4096, 1000000]

    for i in range(len(unidades1)):
        resultado = convertir(i, 1, valores_prueba[i])
        fila = [unidades1[i], unidades2[i], valores_prueba[i], resultado]
        matriz.append(fila)

    for fila in matriz:
        print(fila)

    print("\n--- Fin de las pruebas automáticas ---\n")

