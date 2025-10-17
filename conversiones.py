from Calculadora_Numerico_Avanzado import Calculadora_NumericoAvanzado
from Calculadora_Creativas import  calc_creativas
from Calculadora_Digital import calc_digital
from Calculadora_Fisica import fisicas

def menu_principal():
    print("\n")
    print("======== MENÚ PRINCIPAL ========")
    print("1. Calculadora Numérico Avanzado")
    print("2. Calculadora Fisica")
    print("3. Calculadora Digital")
    print("4. Calculadora Creativa")
    print("5. Salir")

def main():
    while True:
        menu_principal()
        opcion = int(input("Seleccione una opción (1-5): "))
        print("\n")
        if opcion == 1:
            while True:
                Calculadora_Numerico_Avanzado.menu()
                opcion = int(input("Seleccione una opción (1-10): "))
                if opcion == 1:
                    while True:
                        n = int(input("Ingrese un número decimal: "))
                        print(f"Binario: {Calculadora_Numerico_Avanzado.decimal_a_binario(n)}")
                        repetir = input("¿Desea hacer otra conversión Decimal a Binario? (s/n): ").lower()
                        if repetir != "s":
                            break
                elif opcion == 2:
                    while True:
                        b = input("Ingrese un número binario: ")
                        print(f"Decimal: {Calculadora_Numerico_Avanzado.binario_a_decimal(b)}")
                        repetir = input("¿Desea hacer otra conversión Binario a Decimal? (s/n): ").lower()
                        if repetir != "s":
                            break
                elif opcion == 3:
                    while True:
                        n = int(input("Ingrese un número decimal: "))
                        print(f"Octal: {Calculadora_Numerico_Avanzado.decimal_a_octal(n)}")
                        repetir = input("¿Desea hacer otra conversión Decimal a Octal? (s/n): ").lower()
                        if repetir != "s":
                            break
                elif opcion == 4:
                    while True:
                        o = input("Ingrese un número octal: ")
                        print(f"Decimal: {Calculadora_Numerico_Avanzado.octal_a_decimal(o)}")
                        repetir = input("¿Desea hacer otra conversión Octal a Decimal? (s/n): ").lower()
                        if repetir != "s":
                            break
                elif opcion == 5:
                    while True:
                        n = int(input("Ingrese un número decimal: "))
                        print(f"Hexadecimal: {Calculadora_Numerico_Avanzado.decimal_a_hexadecimal(n)}")
                        repetir = input("¿Desea hacer otra conversión Decimal a Hexadecimal? (s/n): ").lower()
                        if repetir != "s":
                            break
                elif opcion == 6:
                    while True:
                        h = input("Ingrese un número hexadecimal: ")
                        print(f"Decimal: {Calculadora_Numerico_Avanzado.hexadecimal_a_decimal(h)}")
                        repetir = input("¿Desea hacer otra conversión Hexadecimal a Decimal? (s/n): ").lower()
                        if repetir != "s":
                            break
                elif opcion == 7:
                    while True:
                        n = int(input("Ingrese un número decimal: "))
                        print(f"Romano: {Calculadora_Numerico_Avanzado.decimal_a_romano(n)}")
                        repetir = input("¿Desea hacer otra conversión Decimal a Romano? (s/n): ").lower()
                        if repetir != "s":
                            break
                elif opcion == 8:
                    while True:
                        r = input("Ingrese un número romano: ")
                        print(f"Decimal: {Calculadora_Numerico_Avanzado.romano_a_decimal(r)}")
                        repetir = input("¿Desea hacer otra conversión Romano a Decimal? (s/n): ").lower()
                        if repetir != "s":
                            break
                elif opcion == 9:
                    Calculadora_Numerico_Avanzado.casos_de_prueba()
                elif opcion == 10:
                    print("Saliendo...")
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
                input("Presione Enter para volver al menú...")
        elif opcion == 2:
            if hasattr(fisicas, "menu"):
                fisicas.menu()
            elif hasattr(fisicas, "calculadora_fisica"):
                fisicas.calculadora_fisica()
            elif hasattr(fisicas, "main"):
                fisicas.main()
            else:
                print("El módulo 'fisicas' no expone main(), calculadora_fisica() ni menu().")
            input("Presione Enter para regresar...")

        
        elif opcion == 3:
            print("\n=== Calculadora Digital ===")
            while True:
                print("\n1. Bytes ↔ Kilobytes")
                print("2. Kilobytes ↔ Megabytes")
                print("3. Megabytes ↔ Gigabytes")
                print("4. bps ↔ Mbps")
                print("5. Ejecutar pruebas automáticas")
                print("6. Regresar al menú principal")

                op_digital = int(input("Seleccione una opción (1-6): "))

                if 1 <= op_digital <= 4:
                    i = op_digital - 1  

                    u1 = calc_digital.unidades1[i]
                    u2 = calc_digital.unidades2[i]
                    f = calc_digital.factores[i]

                    print(f"\nHas elegido convertir entre {u1} y {u2}")
                    print("1.", u1, "→", u2)
                    print("2.", u2, "→", u1)

                    direccion = int(input("Selecciona el sentido de conversión: "))

                    if direccion == 1:
                        valor = float(input(f"Ingrese el número de {u1}: "))
                        resultado = valor / f
                        print(f"\nResultado: {valor} {u1} equivalen a {resultado} {u2}\n")

                    elif direccion == 2:
                        valor = float(input(f"Ingrese el número de {u2}: "))
                        resultado = valor * f
                        print(f"\nResultado: {valor} {u2} equivalen a {resultado} {u1}\n")

                    else:
                        print("Opción inválida.")

                    repetir = input("¿Desea hacer otra conversión digital? (s/n): ").lower()
                    if repetir != "s":
                        break

                elif op_digital == 5:
                    calc_digital.pruebas_codigo()

                elif op_digital == 6:
                    print("Regresando al menú principal...\n")
                    break

                else:
                    print("Opción no válida. Intente de nuevo.")
        elif opcion == 4:
            print("----------CONVERSIONES CREATIVAS--------------")
            while True:
                menu()  # Mostrar menú principal
                opcion = int(input("Elige una opción: "))
        
                # --- Opción 1: Altura en equivalentes de libros ---
                if opcion == 1:
                    while True:
                        print("----------TORRES DE LIBROS----------")
                        print("A cuántos libros equivalen:")
                        altura = pedir_valor()
                        while altura is None:
                            altura = pedir_valor()
        
                        unidades = ['km', 'm', 'cm', 'mm', 'in', 'ft', 'yd', 'mi']
                        unidad = pedir_unidad(unidades)
                        while unidad is None:
                            unidad = pedir_unidad(unidades)
        
                        altura_libros(altura, unidad)
        
                        repetir = input("¿Desea hacer otra conversión de altura? (s/n): ").lower()
                        if repetir != "s":
                            break
        
                # --- Opción 2: Peso en gatos/gatitos ---
                elif opcion == 2:
                    while True:
                        print("----------PESO EN GATOS Y GATITOS----------")
                        print("A cuántos gatos y gatitos equivale:")
                        peso = pedir_valor()
                        while peso is None:
                            peso = pedir_valor()
        
                        unidades = ['ton', 'kg', 'g', 'lb', 'oz', 'slug']
                        unidad = pedir_unidad(unidades)
                        while unidad is None:
                            unidad = pedir_unidad(unidades)
        
                        peso_gatitos(peso, unidad)
        
                        repetir = input("¿Desea hacer otra conversión de peso? (s/n): ").lower()
                        if repetir != "s":
                            break
        
                # --- Opción 3: Energía en barras de chocolate o TNT ---
                elif opcion == 3:
                    while True:
                        print("---------ENERGÍA EN BARRAS DE CHOCOLATE Y TNT---------")
                        print("A cuántas barras o unidades de TNT equivale:")
                        energia = pedir_valor()
                        while energia is None:
                            energia = pedir_valor()
        
                        unidades = ['kcal', 'J', 'kJ', 'kWh', 'BTU']
                        unidad = pedir_unidad(unidades)
                        while unidad is None:
                            unidad = pedir_unidad(unidades)
        
                        energia_en_barras(energia, unidad)
        
                        repetir = input("¿Desea hacer otra conversión de energía? (s/n): ").lower()
                        if repetir != "s":
                            break
        
                # --- Opción 4: Volumen a propiedades de un agujero negro ---
                elif opcion == 4:
                    while True:
                        print("-------VOLUMEN A PROPIEDADES DE UN AGUJERO NEGRO-------")
                        print("Un agujero negro de volumen:")
                        volumen = pedir_valor()
                        while volumen is None:
                            volumen = pedir_valor()
        
                        unidades = ['km', 'm', 'cm', 'mm', 'in', 'ft', 'yd', 'mi', 'l', 'gal']
                        unidad = pedir_unidad(unidades)
                        while unidad is None:
                            unidad = pedir_unidad(unidades)
        
                        vol_agujero_negro(volumen, unidad)
        
                        repetir = input("¿Desea hacer otra conversión de volumen? (s/n): ").lower()
                        if repetir != "s":
                            break
        
                # --- Opción 5: Distancia en equivalentes de animales marinos ---
                elif opcion == 5:
                    while True:
                        print("--------DISTANCIA EQUIVALENTE EN ANIMALES MARINOS-------")
                        print("La distancia es equivalente a:")
                        distancia = pedir_valor()
                        while distancia is None:
                            distancia = pedir_valor()
        
                        unidades = ['km', 'm', 'cm', 'mm', 'in', 'ft', 'yd', 'mi']
                        unidad = pedir_unidad(unidades)
                        while unidad is None:
                            unidad = pedir_unidad(unidades)
        
                        distancia_marina(distancia, unidad)
        
                        repetir = input("¿Desea hacer otra conversión de distancia? (s/n): ").lower()
                        if repetir != "s":
                            break
        
                # --- Opción 6: Pruebas rápidas ---
                elif opcion == 6:
                    print("----PRUEBAS DE LAS FUNCIONES CON VALORES POR DEFAULT----")
                    op = pedir_valor()
                    while op is None:
                        op = pedir_valor()
        
                    pruebas(op)
        
                # --- Opción 7: Salir ---
                elif opcion == 7:
                    print("Saliendo del módulo de conversiones creativas...")
                    break
        
                # --- Entrada no válida ---
                else:
                    print("Opción no válida. Intente de nuevo.")
        elif opcion == 5:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        input("Presione Enter para volver al menú...")

main()
