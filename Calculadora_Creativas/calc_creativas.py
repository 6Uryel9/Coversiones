import math
import random

# Constantes físicas
GRAVEDAD = 6.6674 * 10**-11   # Constante de gravitación universal (N·m²/kg²)
VEL_LUZ = 3 * 10**8           # Velocidad de la luz en el vacío (m/s)


def menu():
    """Muestra las opciones disponibles en el menú principal."""
    print("Estas son algunas de las ideas que puedes explorar:")
    print("1. Altura en torres de libros")
    print("2. Peso equivalente en gatitos")
    print("3. Energía equivalente en barras de chocolate y toneladas de TNT")
    print("4. Volumen a propiedades de un agujero negro")
    print("5. Distancia en animales marinos")
    print("6. Pruebas con valores estándar")
    print("7. Salir")
    print("=" * 70)


def altura_libros(altura, unidad):
    """
    Convierte una altura en diferentes unidades a la cantidad equivalente
    de libros 'Don Quijote' y 'El Principito' que formarían esa torre.

    - Cada libro del Quijote mide 8 cm.
    - Cada libro del Principito mide 1 cm.
    """
    # Lista bidimensional: [unidad, factor para convertir a centímetros]
    conversiones = [
        ["km", 100000],
        ["m", 100],
        ["cm", 1],
        ["mm", 0.1],
        ["in", 2.54],
        ["ft", 30.48],
        ["yd", 91.44],
        ["mi", 160934]
    ]

    cem = None
    for u, factor in conversiones:
        if unidad == u:
            cem = altura * factor
            break

    if cem is None:
        print("Unidad no reconocida.")
        return

    # Número de libros equivalentes
    quijote = int(cem // 8)
    principito = int(cem // 1)

    print("La torre de libros tendría:")
    print(quijote, " Libros del Quijote de la Mancha")
    print("Y...")
    print(principito, " Libros del Principito")


def peso_gatitos(peso, unidad):
    """
    Convierte un peso en diferentes unidades al equivalente en gatos adultos
    y gatitos pequeños.

    - Un gato adulto pesa 4 kg.
    - Un gatito pesa 1.5 kg.
    """
    conversiones = [
        ["ton", 1000],
        ["kg", 1],
        ["g", 0.001],
        ["lb", 0.45359237],
        ["oz", 0.0283495231],
        ["slug", 14.5939]
    ]

    kilo = None
    for u, factor in conversiones:
        if unidad == u:
            kilo = peso * factor
            break

    if kilo is None:
        print("Unidad no reconocida.")
        return

    gatos = int(kilo // 4)
    gatitos = int(kilo // 1.5)

    print("Por ese peso tendrías:")
    print(gatos, " Gatos adultos de 4 kg")
    print("Y...")
    print(gatitos, " Gatitos de 1.5 kg")


def energia_en_barras(energia, unidad):
    """
    Convierte una cantidad de energía a su equivalente en barras de chocolate
    y toneladas de TNT.

    - Ferrero Rocher = 73 kcal
    - Hershey's = 210 kcal
    - Carlos V = 140 kcal
    - Tonelada de TNT ≈ 1,000,000 kcal
    """
    conversiones = [
        ["kcal", 1],
        ["J", 1 / 4184],
        ["kJ", 1 / 4.184],
        ["kWh", 860.4],
        ["BTU", 0.252]
    ]

    kcal = None
    for u, factor in conversiones:
        if unidad == u:
            kcal = energia * factor
            break

    if kcal is None:
        print("Unidad no reconocida.")
        return

    ferrero = kcal / 73
    hersheys = kcal / 210
    carlos = kcal / 140
    ton_tnt = kcal / 10**6

    print("Tendrías:")
    print(f"{ferrero:.2f}", " piezas de Ferrero Rocher")
    print(f"{hersheys:.2f}", " barras de Hershey's")
    print(f"{carlos:.2f}", " barritas de Carlos V")
    print("Y...")
    print(f"{ton_tnt:.2f}", " toneladas de TNT")


def vol_agujero_negro(volumen, unidad):
    """
    Calcula las propiedades físicas de un agujero negro
    a partir de un volumen dado:

    - Radio del agujero negro
    - Masa equivalente
    - Dilatación temporal cerca del horizonte de sucesos
    """
    conversiones = [
        ["km", 10**9],
        ["m", 1],
        ["cm", 1 / 10**6],
        ["mm", 1 / 10**9],
        ["in", 0.0254**3],
        ["ft", 0.3048**3],
        ["yd", 0.9144**3],
        ["mi", 1609.34**3],
        ["l", 0.001],
        ["gal", 0.003785]
    ]

    mtr = None
    for u, factor in conversiones:
        if unidad == u:
            mtr = volumen * factor
            break

    if mtr is None:
        print("Unidad no reconocida.")
        return

    # Cálculos físicos
    radio = ((mtr * 3) / (4 * math.pi)) ** (1 / 3)
    masa = (radio * VEL_LUZ ** 2) / (2 * GRAVEDAD)

    r_obs = radio * 1.5
    dif = 1 - (radio / r_obs)
    tiempo = math.sqrt(dif) * 60

    print("Propiedades del Agujero Negro:")
    print(f"Radio equivalente: {radio:.2f} m")
    print(f"Masa: {masa:.2e} kg")
    print(f"Tiempo cerca del horizonte: {tiempo:.2f} min (vs 1 hora en la Tierra)")


def distancia_marina(distancia, unidad):
    """
    Convierte una distancia en diversas unidades a metros,
    luego la descompone en equivalentes de animales marinos.
    """
    conversiones = [
        ["km", 1000],
        ["m", 1],
        ["cm", 0.01],
        ["mm", 0.001],
        ["in", 0.0254],
        ["ft", 0.3048],
        ["yd", 0.9144],
        ["mi", 1609.34]
    ]

    mtr = None
    for u, factor in conversiones:
        if unidad == u:
            mtr = distancia * factor
            break

    if mtr is None:
        print("Unidad no reconocida.")
        return

    especies = [
        ("Ballenas azules", 24),
        ("Calamares gigantes", 10),
        ("Orcas", 6),
        ("Tiburones blancos", 4),
        ("Delfines", 2),
        ("Tortugas", 1),
        ("Medusas", 0.2),
        ("Caballitos de mar", 0.06),
        ("Krill", 0.01),
        ("Rotíferos", 0.001)
    ]

    resultado = {}
    for nombre, valor in especies:
        if mtr >= valor:
            cantidad = int(mtr // valor)
            mtr %= valor
            resultado[nombre] = cantidad
        else:
            resultado[nombre] = 0

    print("Equivale a esta cantidad de animales marinos:")
    for nombre, cantidad in resultado.items():
        print(f"{nombre}: {cantidad}")

def pruebas(op):
    """
    Ejecuta pruebas rápidas con valores predefinidos
    para verificar el funcionamiento de las funciones principales.
    """
        while True:
        print("Tu opción es...")
        op = pedir_valor()
        while op is None:
            op = pedir_valor()
        if op == 1:
            altura = 2.3
            unidad = 'm'
            print("FUNCIÓN: altura_libros(altura, unidad)")
            print(f"Parámetros: altura = {altura} {unidad}")
            esperado = f"Equivalente a una torre de aproximadamente {int((altura * 100) // 8)} libros del Quijote o {int((altura * 100) // 1)} libros del Principito."
            print(f"Resultado esperado: {esperado}\n")
            print(f"Y tú has obtenido:")
            altura_libros(altura, unidad)
            print("=" * 70)

        elif op == 2:
            peso = 87755
            unidad = 'g'
            print("FUNCIÓN: peso_gatitos(peso, unidad)")
            print(f"Parámetros: peso = {peso} {unidad}")
            esperado = f"Equivalente a aproximadamente {int((peso * 0.001) // 4)} gatos adultos o {int((peso * 0.001) // 1.5)} gatitos."
            print(f"Resultado esperado: {esperado}\n")
            print(f"Y tú has obtenido:")
            peso_gatitos(peso, unidad)
            print("=" * 70)

        elif op == 3:
            energia = 2000
            unidad = 'kWh'
            print("FUNCIÓN: energia_en_barras(energia, unidad)")
            print(f"Parámetros: energía = {energia} {unidad}")
            esperado = "Equivalente a miles de barras de chocolate o unas pocas toneladas de TNT."
            print(f"Resultado esperado: {esperado}\n")
            print(f"Y tú has obtenido:")
            energia_en_barras(energia, unidad)
            print("=" * 70)

        elif op == 4:
            volumen = 1
            unidad = 'km'
            print("FUNCIÓN: vol_agujero_negro(volumen, unidad)")
            print(f"Parámetros: volumen = {volumen} {unidad}³")
            esperado = "Debería mostrar un radio y una masa extremadamente grandes, representando un agujero negro teórico."
            print(f"Resultado esperado: {esperado}\n")
            print(f"Y tú has obtenido:")
            vol_agujero_negro(volumen, unidad)
            print("=" * 70)

        elif op == 5:
            distancia = 47.271
            unidad = 'm'
            print("FUNCIÓN: distancia_marina(distancia, unidad)")
            print(f"Parámetros: distancia = {distancia} {unidad}")
            esperado = "Equivalente a una combinación de longitudes de animales marinos, desde ballenas hasta caballitos de mar."
            print(f"Resultado esperado: {esperado}\n")
            print(f"Y tú has obtenido:")
            distancia_marina(distancia, unidad)
            print("=" * 70)

        else:
            print("Opción no válida. Intenta de nuevo")
            continue

        repetir = input("¿Desea hacer otra consulta? (s/n):").lower()
        if repetir != "s":
            return None

def escenario_aleatorio(categoria):
    """
    Lee el archivo 'escenarios.txt' y devuelve un escenario aleatorio de la categoría solicitada.
    Categorías: 'ALTURA', 'PESO', 'ENERGIA', 'AGUJERO', 'DISTANCIA'
    """
    bloques = {}
    try:
        with open("escenarios.txt", "r", encoding="utf-8") as f:
            key = None
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line.startswith("[") and line.endswith("]"):
                    key = line[1:-1].upper()
                    bloques[key] = []
                elif key:
                    bloques[key].append(line)
    except FileNotFoundError:
        print("El archivo 'escenarios.txt' no se encontró.")
        return None

    if categoria.upper() in bloques:
        return random.choice(bloques[categoria.upper()])
    else:
        return None

def pedir_valor():
    """
    Solicita al usuario un valor numérico positivo.
    Retorna:
        float: el valor ingresado si es válido.
        None: si el valor es menor o igual a 0.
    """
    valor = float(input("Ingresa un valor: "))
    if valor <= 0:
        print("Valor no reconocido")
        return None
    else:
        return valor

def pedir_unidad(unidades):
    """
    Solicita al usuario una unidad de medida entre las disponibles.
    Parámetros:
        unidades (list): lista de unidades válidas.
    Retorna:
        str: la unidad seleccionada si es válida.
        None: si no se reconoce la unidad.
    """
    print("Unidades disponibles:", ", ".join(unidades))
    unidad = input("Ingresa una unidad: ").strip().lower()

    # Convertimos la lista de unidades a minúsculas para comparar
    unidades_minusculas = [u.lower() for u in unidades]
    if unidad in unidades_minusculas:
        return unidad
    print("Unidad no reconocida...")
    return None
