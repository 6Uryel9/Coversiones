#Es el menu donde eliges que accion quieres hacer 
def menu():
    print("Conversiones fisicas")
    print("Unidades de DISTANCIA: km, m, cm, mm")
    print("Unidades de TEMPERATURA: C, F, K")
    print("1. Convertir distancia")
    print("2. Tabla rápida de distancia (a km, m, cm, mm)")
    print("3. Convertir temperatura")
    print("4. Tabla rápida de temperatura (a C, F, K)")
    print("5. Pruebas con valores estándar")
    print("6. Salir")

#Es el conversor de distancia, eliges num y a que distancia la quieres convertir, usa tu valor y lo multiplica por tu factor de origen para despues divir el resultado de eso entre el factor de destino que elegiste 
def conv_distancia(valor, origen, destino):
    if origen == 'km':
        factor_origen = 1000.0
    elif origen == 'm':
        factor_origen = 1.0
    elif origen == 'cm':
        factor_origen = 0.01
    elif origen == 'mm':
        factor_origen = 0.001
    else:
        print("Unidad origen no reconocida (usa km, m, cm, mm)")
        return None

    if destino == 'km':
        factor_destino = 1000.0
    elif destino == 'm':
        factor_destino = 1.0
    elif destino == 'cm':
        factor_destino = 0.01
    elif destino == 'mm':
        factor_destino = 0.001
    else:
        print("Unidad destino no reconocida (usa km, m, cm, mm)")
        return None

    metros = valor * factor_origen
    resultado = metros / factor_destino
    return resultado
#te hace una tabla con las diferentes distancias que hay, le das un valor y te la transforma en las distancias que tiene el programa.
def tabla_distancia(valor, origen):

    matriz = [["unidad", "valor"]]
    matriz.append(["km", conv_distancia(valor, origen, 'km')])
    matriz.append(["m",  conv_distancia(valor, origen, 'm')])
    matriz.append(["cm", conv_distancia(valor, origen, 'cm')])
    matriz.append(["mm", conv_distancia(valor, origen, 'mm')])

    print("\nTabla rápida de DISTANCIA (desde", valor, origen, ")")
    for fila in matriz[1:]:
        print(f"{fila[0]}: {fila[1]}")
    return matriz

# similar al converson de distancia pero este hace la operacion en base a la temperatura de destino que elijas.
def conv_temperatura(valor, origen, destino):
    if origen == 'C':
        c = valor
    elif origen == 'F':
        c = (valor - 32.0) * 5.0/9.0
    elif origen == 'K':
        c = valor - 273.15
    else:
        print("Unidad origen no reconocida (usa C, F, K)")
        return None

    if destino == 'C':
        return c
    elif destino == 'F':
        return c * 9.0/5.0 + 32.0
    elif destino == 'K':
        return c + 273.15
    else:
        print("Unidad destino no reconocida (usa C, F, K)")
        return None
# te hace una tabla con el valor que le proporciones a las diferentes temperaturas que tiene el programa 
def tabla_temperatura(valor, origen):
    matriz = [["unidad", "valor"]]
    matriz.append(["C", conv_temperatura(valor, origen, 'C')])
    matriz.append(["F", conv_temperatura(valor, origen, 'F')])
    matriz.append(["K", conv_temperatura(valor, origen, 'K')])

    print("\nTabla rápida de TEMPERATURA (desde", valor, origen, ")")
    for fila in matriz[1:]:
        print(f"{fila[0]}: {fila[1]}")
    return matriz



def pedir_valor():
    valor = float(input("Ingresa un valor: "))
    return valor

def pedir_unidad_dist():
    unidad = input("Ingresa una UNIDAD DE DISTANCIA (km/m/cm/mm): ")
    if unidad == 'km' or unidad == 'm' or unidad == 'cm' or unidad == 'mm':
        return unidad
    else:
        print("Unidad no reconocida (usa km, m, cm, mm)")
        return None

def pedir_unidad_temp():
    unidad = input("Ingresa una UNIDAD DE TEMPERATURA (C/F/K): ")
    if unidad == 'C' or unidad == 'F' or unidad == 'K':
        return unidad
    else:
        print("Unidad no reconocida (usa C, F, K)")
        return None



def pruebas(op):
    if op == 1:
        print(conv_distancia(2500, 'm', 'cm'))
    elif op == 2:
        _ = tabla_distancia(1.75, 'km')
    elif op == 3:
        print(conv_temperatura(25, 'C', 'F'))
    elif op == 4:
        _ = tabla_temperatura(300, 'K')
    else:
        print("No se pudo realizar la consulta. Intenta de nuevo")


def main():
    while True:
        menu()
        op = int(input("Elige una opción: "))

        if op == 1:
            print("Conversión de distancia (km, m, cm, mm)")
            valor = pedir_valor()
            u1 = pedir_unidad_dist()
            while u1 is None:
                u1 = pedir_unidad_dist()
            u2 = pedir_unidad_dist()
            while u2 is None:
                u2 = pedir_unidad_dist()
            r = conv_distancia(valor, u1, u2)
            if r is not None:
                print(valor, u1, "=", r, u2)

        elif op == 2:
            print("Tabla rápida (distancia)")
            valor = pedir_valor()
            u1 = pedir_unidad_dist()
            while u1 is None:
                u1 = pedir_unidad_dist()
            _ = tabla_distancia(valor, u1)  

        elif op == 3:
            print("Conversión de temperatura (C, F, K)")
            valor = pedir_valor()
            u1 = pedir_unidad_temp()
            while u1 is None:
                u1 = pedir_unidad_temp()
            u2 = pedir_unidad_temp()
            while u2 is None:
                u2 = pedir_unidad_temp()
            r = conv_temperatura(valor, u1, u2)
            if r is not None:
                print(valor, u1, "=", r, u2)

        elif op == 4:
            print("Tabla rápida (temperatura)")
            valor = pedir_valor()
            u1 = pedir_unidad_temp()
            while u1 is None:
                u1 = pedir_unidad_temp()
            _ = tabla_temperatura(valor, u1)

        elif op == 5:
            print("Pruebas con valores estándar")
            print("1) Distancia puntual | 2) Distancia tabla | 3) Temp puntual | 4) Temp tabla")
            sub = int(input("Elige prueba: "))
            pruebas(sub)

        elif op == 6:
            print("Nos vemos, mi inge")
            return

        else:
            print("Opción inválida")

def calculadora_fisica():
    return main()

def dispatch(op):
    """
    Opcional: si en algún momento solo llamas fisicas.menu()
    y luego quieres que el main grande lea 'op' y despache aquí.
    """
    if op == 1:
        print("Conversión de distancia (km, m, cm, mm)")
        valor = pedir_valor()
        u1 = pedir_unidad_dist()
        while u1 is None:
            u1 = pedir_unidad_dist()
        u2 = pedir_unidad_dist()
        while u2 is None:
            u2 = pedir_unidad_dist()
        r = conv_distancia(valor, u1, u2)
        if r is not None:
            print(valor, u1, "=", r, u2)

    elif op == 2:
        print("Tabla rápida (distancia)")
        valor = pedir_valor()
        u1 = pedir_unidad_dist()
        while u1 is None:
            u1 = pedir_unidad_dist()
        _ = tabla_distancia(valor, u1)

    elif op == 3:
        print("Conversión de temperatura (C, F, K)")
        valor = pedir_valor()
        u1 = pedir_unidad_temp()
        while u1 is None:
            u1 = pedir_unidad_temp()
        u2 = pedir_unidad_temp()
        while u2 is None:
            u2 = pedir_unidad_temp()
        r = conv_temperatura(valor, u1, u2)
        if r is not None:
            print(valor, u1, "=", r, u2)

    elif op == 4:
        print("Tabla rápida (temperatura)")
        valor = pedir_valor()
        u1 = pedir_unidad_temp()
        while u1 is None:
            u1 = pedir_unidad_temp()
        _ = tabla_temperatura(valor, u1)

    elif op == 5:
        print("Pruebas con valores estándar")
        print("1) Distancia puntual | 2) Distancia tabla | 3) Temp puntual | 4) Temp tabla")
        sub = int(input("Elige prueba: "))
        pruebas(sub)

    elif op == 6:
        print("Nos vemos, mi inge")
        return

    else:
        print("Opción inválida")




