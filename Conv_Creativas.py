import math

gravedad=6.6674*10**-11
vel_luz=3*10**8

def menu():
    print("Estas son algunas de las ideas que puedes explorar:")
    print("1. Altura en torres de libros")
    print("2. Peso equivalente en gatitos")
    print("3. Energía equivalente en barras de chocolate y toneladas de TNT")
    print("4. Volumen a propiedades de un agujero negro")
    print("5. Distancia en animales marinos")
    print("6. Pruebas con valores estándar")
    print("7. Salir")

def altura_libros(altura,unidad):
    cem=0
    res = 0

    if unidad == 'km':
        cem = altura* 100000
    elif unidad == 'm':
        cem = altura*100
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

    if cem>=8:
        quijote=int(cem//8)
        res=cem%8
    else:
        quijote=0
        res=cem
    if res>=1:
        principito=int(res//1)
    else:
        principito=0

    print("La torre de libros tendría: ")
    print(quijote," Libros del Quijote de la mancha")
    print(principito," Libros del Princpito")

def peso_gatitos(peso,unidad):
    kilo=0
    res = 0
    gatos=0
    gatitos=0

    if unidad == 'ton':
        kilo = peso * 1000
    elif unidad == 'kg':
        kilo = peso
    elif unidad == 'g':
        kilo = peso/1000
    elif unidad == 'lb':
        kilo = peso*0.45359237
    elif unidad == 'oz':
        kilo = peso*0.0283495231
    elif unidad == 'slug':
        kilo = peso*14.5939

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
    print(int(gatos)," Gatos adultos de 4 kg")
    print(int(gatitos)," Gatitos de 1.5 kg")

def energia_en_barras(energia,unidad):
    kcal=0
    ferrero=0
    hersheys=0
    carlos=0
    ton_tnt=0

    if unidad=='kcal':
        kcal=energia
    elif unidad == 'J':
        kcal = energia/4184
    elif unidad == 'kJ':
        kcal = energia/4.184
    elif unidad=='kWh':
        kcal = energia*860.4
    elif unidad =='BTU':
        kcal = energia*0.252

    ferrero=kcal/73
    hersheys=kcal/210
    carlos=kcal/140
    ton_tnt=kcal/10**6

    print("Tendrías:")
    print(f"{ferrero:.2f}"," piezas de Ferrero Rocher")
    print(f"{hersheys:.2f}"," barras de Hersheys")
    print(f"{carlos:.2f}"," barritas de Carlos v")
    print(f"{ton_tnt:2f}"," toneladas de TNT")

def vol_agujero_negro(volumen,unidad):
    mtr=0
    radio = 0
    masa = 0
    r_obs = 0
    dif = 0
    varia = 0
    tiempo = 0

    if unidad == 'km':
        mtr = (volumen * 10**9)
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
        mtr = volumen*0.001
    elif unidad == 'gal':
        mtr = volumen*0.003785

    radio = ((mtr*3)/(math.pi*4))**(1/3)
    numerador = math.pow(vel_luz,2)*radio
    masa=numerador/(2*gravedad)
    r_obs = radio*1.5
    dif = 1-(radio/r_obs)
    varia = math.sqrt(dif)
    tiempo = varia*60

    print("Tendría:")
    print(f"{radio:.2f}","m de radio")
    print(f"{masa:.2f}","kg de masa")
    print("Y cerca de él transcurrirían ", f"{tiempo:.2f}"," minutos,"
        " mientras en la tierra transcurriría 1 hora")

def distancia_marina(distancia, unidad):
    if unidad == 'km':
        mtr = distancia * 1000
    elif unidad == 'm':
        mtr = distancia
    elif unidad == 'cm':
        mtr = distancia / 100
    elif unidad == 'mm':
        mtr = distancia / 1000
    elif unidad == 'in':
        mtr = distancia * 0.0254
    elif unidad == 'ft':
        mtr = distancia * 0.3048
    elif unidad == 'yd':
        mtr = distancia * 0.9144
    elif unidad == 'mi':
        mtr = distancia * 1609.34

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

    resultado = {}
    for nombre,valor in especies:
        if mtr >= valor:
            cantidad = mtr // valor
            mtr = mtr % valor
            resultado[nombre] = int(cantidad)
        else:
            resultado[nombre] = 0

    print("Equivale a esta cantidad de animales marinos: ")
    for nombre in resultado:
        print(nombre,": ", resultado[nombre])

def pruebas(op):
    if op==1:
        print(altura_libros(2.3,'m'))
    elif op==2:
        print(peso_gatitos(87755,'g'))
    elif op==3:
        print(energia_en_barras(2000,'kWh'))
    elif op==4:
        print(vol_agujero_negro(1,'km'))
    elif op==5:
        distancia_marina(47.271,'m')
    else:
        print("No se pudo realizar la consulta. Intenta de nuevo")

def pedir_valor():
    valor = float(input("Ingresa un valor: "))
    if valor <= 0:
        print("Valor no reconocido")
        return None
    else:
        return valor

def pedir_unidad(unidades):
    print("Unidades: ", unidades)
    unidad = str(input("Ingresa un unidad: "))
    if unidad in unidades:
        return unidad
    else:
        print("Unidad no reconocida")
        return None

def regresar_menu():
    print("Presiona Enter para regresar al menú, "
          "o cualquier otra tecla para salir")
    valor=input()
    if valor == "":
        return None
    else:
        return False

def main():
    menu()
    while True:
        op=int(input("Elige una opción: "))
        if op==1:
            print("A cuántos libros equivalen:")
            altura=pedir_valor()
            while altura is None:
                altura=pedir_valor()
            unidades = ['km', 'm', 'cm', 'mm', 'in', 'ft', 'yd', 'mi']
            unidad=pedir_unidad(unidades)
            while unidad is None:
                unidad=pedir_unidad(unidades)
            altura_libros(altura,unidad)
            valor=regresar_menu()
            if valor is None:
                continue
            else:
                break
        elif op==2:
            print("A cuántos Gatos y Gatitos equivalen:")
            peso = pedir_valor()
            while peso is None:
                peso = pedir_valor()
            unidades = ['ton','kg','g','lb','oz','slug']
            unidad = pedir_unidad(unidades)
            while unidad is None:
                unidad = pedir_unidad(unidades)
            peso_gatitos(peso, unidad)
            valor = regresar_menu()
            if valor is None:
                continue
            else:
                break
        elif op==3:
            print("A cuántas barras o tTNT equivalen:")
            energia = pedir_valor()
            while energia is None:
                energia = pedir_valor()
            unidades = ['kcal', 'J', 'kJ', 'kWh', 'BTU']
            unidad = pedir_unidad(unidades)
            while unidad is None:
                unidad = pedir_unidad(unidades)
            energia_en_barras(energia,unidad)
            valor = regresar_menu()
            if valor is None:
                continue
            else:
                break
        elif op==4:
            print("Un Agujero Negro de volumen:")
            volumen = pedir_valor()
            while volumen is None:
                volumen = pedir_valor()
            unidades = ['km', 'm', 'cm', 'mm', 'in', 'ft', 'yd', 'mi', 'l', 'gal']
            unidad = pedir_unidad(unidades)
            while unidad is None:
                unidad = pedir_unidad(unidades)
            vol_agujero_negro(volumen,unidad)
            valor = regresar_menu()
            if valor is None:
                continue
            else:
                break
        elif op==5:
            Print("La distancia:")
            distancia = pedir_valor()
            while distancia is None:
                distancia = pedir_valor()
            unidades = ['km', 'm', 'cm', 'mm', 'in', 'ft', 'yd', 'mi']
            unidad = pedir_unidad(unidades)
            while unidad is None:
                unidad = pedir_unidad(unidades)
            distancia_marina(distancia,unidad)
            valor = regresar_menu()
            if valor is None:
                continue
            else:
                break
        elif op==6:
            op=pedir_valor()
            while op is None:
                op = pedir_valor()
            pruebas(op)
            valor = regresar_menu()
            if valor is None:
                continue
            else:
                break
        elif op==7:
            print ("Has salido con éxito, gracias por tu visista.")
            break
        else:
            print("Opcion no valida")

main()