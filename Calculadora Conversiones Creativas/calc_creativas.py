import math

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


def altura_libros(altura, unidad):
    """
    Convierte una altura en diferentes unidades a la cantidad equivalente
    de libros 'Don Quijote' y 'El Principito' que formarían esa torre.

    - Cada libro del Quijote mide 8 cm.
    - Cada libro del Principito mide 1 cm.
    """
    cem = 0

    # Conversión de unidades a centímetros
    if unidad == 'km':
        cem = altura * 100000
    elif unidad == 'm':
        cem = altura * 100
    elif unidad == 'cm':
        cem = altura
    elif unidad == 'mm':
        cem = altura / 10
    elif unidad == 'in':
        cem = altura * 2.54
    elif unidad == 'ft':
        cem = altura * 30.48
    elif unidad == 'yd':
        cem = altura * 91.44
    elif unidad == 'mi':
        cem = altura * 160934

    # Número de libros equivalentes
    if cem >= 8:
        quijote = int(cem // 8)
        res = cem % 8
    else:
        quijote = 0
        res = cem

    if res >= 1:
        principito = int(res // 1)
    else:
        principito = 0

    print("La torre de libros tendría: ")
    print(quijote, " Libros del Quijote de la Mancha")
    print(principito, " Libros del Principito")


def peso_gatitos(peso, unidad):
    """
    Convierte un peso en diferentes unidades al equivalente en gatos adultos
    y gatitos pequeños.

    - Un gato adulto pesa 4 kg.
    - Un gatito pesa 1.5 kg.
    """
    kilo = 0

    # Conversión de unidades a kilogramos
    if unidad == 'ton':
        kilo = peso * 1000
    elif unidad == 'kg':
        kilo = peso
    elif unidad == 'g':
        kilo = peso / 1000
    elif unidad == 'lb':
        kilo = peso * 0.45359237
    elif unidad == 'oz':
        kilo = peso * 0.0283495231
    elif unidad == 'slug':
        kilo = peso * 14.5939

    # Número de gatos y gatitos
    if kilo >= 4:
        gatos = kilo // 4
        res = kilo % 4
    else:
        gatos = 0
        res = kilo

    if res >= 1.5:
        gatitos = res // 1.5
    else:
        gatitos = 0

    print("Por ese peso tendrías:")
    print(int(gatos), " Gatos adultos de 4 kg")
    print(int(gatitos), " Gatitos de 1.5 kg")


def energia_en_barras(energia, unidad):
    """
    Convierte una cantidad de energía a su equivalente en barras de chocolate
    y toneladas de TNT.

    - Ferrero Rocher = 73 kcal
    - Hershey's = 210 kcal
    - Carlos V = 140 kcal
    - Tonelada de TNT ≈ 1,000,000 kcal
    """
    kcal = 0

    # Conversión de unidades a kilocalorías
    if unidad == 'kcal':
        kcal = energia
    elif unidad == 'J':
        kcal = energia / 4184
    elif unidad == 'kJ':
        kcal = energia / 4.184
    elif unidad == 'kWh':
        kcal = energia * 860.4
    elif unidad == 'BTU':
        kcal = energia * 0.252

    # Equivalencias
    ferrero = kcal / 73
    hersheys = kcal / 210
    carlos = kcal / 140
    ton_tnt = kcal / 10**6

    print("Tendrías:")
    print(f"{ferrero:.2f}", " piezas de Ferrero Rocher")
    print(f"{hersheys:.2f}", " barras de Hershey's")
    print(f"{carlos:.2f}", " barritas de Carlos V")
    print(f"{ton_tnt:.2f}", " toneladas de TNT")


def vol_agujero_negro(volumen, unidad):
    """
    Calcula las propiedades físicas de un agujero negro
    a partir de un volumen dado:

    - Radio del agujero negro
    - Masa equivalente
    - Dilatación temporal cerca del horizonte de sucesos
    """

    # Conversión de unidades a metros cúbicos
    if unidad == 'km':
        mtr = volumen * 10**9
    elif unidad == 'm':
        mtr = volumen
    elif unidad == 'cm':
        mtr = volumen / 10**6
    elif unidad == 'mm':
        mtr = volumen / 10**9
    elif unidad == 'in':
        mtr = volumen * 0.0254**3
    elif unidad == 'ft':
        mtr = volumen * 0.3048**3
    elif unidad == 'yd':
        mtr = volumen * 0.9144**3
    elif unidad == 'mi':
        mtr = volumen * 1609.34**3
    elif unidad == 'l':
        mtr = volumen * 0.001
    elif unidad == 'gal':
        mtr = volumen * 0.003785

    # Cálculos físicos
    # Radio equivalente al volumen (esfera)
    radio = ((mtr * 3) / (4 * math.pi)) ** (1 / 3)

    # Masa del agujero negro (fórmula del radio de Schwarzschild despejada)
    masa = (radio * VEL_LUZ ** 2) / (2 * GRAVEDAD)

    # Horizonte de sucesos
    r_s = (2 * GRAVEDAD * masa) / (VEL_LUZ ** 2)

    # Dilatación temporal: relación tiempo exterior / tiempo cerca del horizonte
    radio = ((mtr * 3) / (math.pi * 4)) ** (1 / 3)
    numerador = math.pow(VEL_LUZ, 2) * radio
    masa = numerador / (2 * GRAVEDAD)
    r_obs = radio * 1.5
    dif = 1 - (radio / r_obs)
    varia = math.sqrt(dif)
    tiempo = varia * 60

    # Resultados
    print("Propiedades del Agujero Negro:")
    print(f"Radio equivalente: {radio:.2f} m")
    print(f"Masa: {masa:.2e} kg")  # notación científica base 10
    print(f"Tiempo cerca del horizonte: {tiempo:.2f} min (vs 1 hora en la Tierra)")

def distancia_marina(distancia, unidad):
    mtr=0
    # Conversión de la distancia ingresada a metros
    if unidad == 'km':
        mtr = distancia * 1000  # kilómetros a metros
    elif unidad == 'm':
        mtr = distancia  # ya está en metros
    elif unidad == 'cm':
        mtr = distancia / 100  # centímetros a metros
    elif unidad == 'mm':
        mtr = distancia / 1000  # milímetros a metros
    elif unidad == 'in':
        mtr = distancia * 0.0254  # pulgadas a metros
    elif unidad == 'ft':
        mtr = distancia * 0.3048  # pies a metros
    elif unidad == 'yd':
        mtr = distancia * 0.9144  # yardas a metros
    elif unidad == 'mi':
        mtr = distancia * 1609.34  # millas a metros

    # Lista de especies con su tamaño de referencia en metros
    # Ejemplo: 1 ballena azul equivale a 24 m de distancia
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
        ("Rotiferos", 0.001)
    ]

    # Diccionario para guardar los resultados
    resultado = {}

    # Descomposición de la distancia en unidades equivalentes a los animales
    for nombre, valor in especies:
        if mtr >= valor:
            cantidad = mtr // valor  # cuántos caben completos
            mtr = mtr % valor  # resto de la distancia
            resultado[nombre] = int(cantidad)
        else:
            resultado[nombre] = 0  # si no cabe ninguno, queda en 0

    # Mostrar los resultados finales
    print("Equivale a esta cantidad de animales marinos: ")
    for nombre in resultado:
        print(nombre, ": ", resultado[nombre])

def pruebas(op):
    """
    Ejecuta pruebas rápidas con valores predefinidos
    para verificar el funcionamiento de las funciones principales.

    Parámetros:
        op (int): número de la opción de prueba.
    """
    if op == 1:
        print(altura_libros(2.3, 'm'))  # Torre de libros para 2.3 m
    elif op == 2:
        print(peso_gatitos(87755, 'g'))  # Peso de 87,755 g en gatos/gatitos
    elif op == 3:
        print(energia_en_barras(2000, 'kWh'))  # Energía de 2000 kWh en equivalencias
    elif op == 4:
        print(vol_agujero_negro(1, 'km'))  # Agujero negro de volumen 1 km³
    elif op == 5:
        distancia_marina(47.271, 'm')  # Distancia de 47.271 m en animales marinos
    else:
        print("No se pudo realizar la consulta. Intenta de nuevo")

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
    print("Unidades: ", unidades)
    unidad = str(input("Ingresa una unidad: "))
    if unidad in unidades:
        return unidad
    else:
        print("Unidad no reconocida")
        return None
