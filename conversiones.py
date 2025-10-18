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
                Calculadora_NumericoAvanzado.menu()
                opcion = int(input("Seleccione una opción (1-10): "))
                if opcion == 1:
                    while True:
                        n = int(input("Ingrese un número decimal: "))
                        print(f"Binario: {Calculadora_NumericoAvanzado.decimal_a_binario(n)}")
                        repetir = input("¿Desea hacer otra conversión Decimal a Binario? (s/n): ").lower()
                        if repetir != "s":  
                            break
                elif opcion == 2:
                    while True:
                        b = input("Ingrese un número binario: ")
                        print(f"Decimal: {Calculadora_NumericoAvanzado.binario_a_decimal(b)}")
                        repetir = input("¿Desea hacer otra conversión Binario a Decimal? (s/n): ").lower()
                        if repetir != "s":
                            break
                elif opcion == 3:
                    while True:
                        n = int(input("Ingrese un número decimal: "))
                        print(f"Octal: {Calculadora_NumericoAvanzado.decimal_a_octal(n)}")
                        repetir = input("¿Desea hacer otra conversión Decimal a Octal? (s/n): ").lower()
                        if repetir != "s":
                            break
                elif opcion == 4:
                    while True:
                        o = input("Ingrese un número octal: ")
                        print(f"Decimal: {Calculadora_NumericoAvanzado.octal_a_decimal(o)}")
                        repetir = input("¿Desea hacer otra conversión Octal a Decimal? (s/n): ").lower()
                        if repetir != "s":
                            break
                elif opcion == 5:
                    while True:
                        n = int(input("Ingrese un número decimal: "))
                        print(f"Hexadecimal: {Calculadora_NumericoAvanzado.decimal_a_hexadecimal(n)}")
                        repetir = input("¿Desea hacer otra conversión Decimal a Hexadecimal? (s/n): ").lower()
                        if repetir != "s":
                            break
                elif opcion == 6:
                    while True:
                        h = input("Ingrese un número hexadecimal: ")
                        print(f"Decimal: {Calculadora_NumericoAvanzado.hexadecimal_a_decimal(h)}")
                        repetir = input("¿Desea hacer otra conversión Hexadecimal a Decimal? (s/n): ").lower()
                        if repetir != "s":
                            break
                elif opcion == 7:
                    while True:
                        n = int(input("Ingrese un número decimal: "))
                        print(f"Romano: {Calculadora_NumericoAvanzado.decimal_a_romano(n)}")
                        repetir = input("¿Desea hacer otra conversión Decimal a Romano? (s/n): ").lower()
                        if repetir != "s":
                            break
                elif opcion == 8:
                    while True:
                        r = input("Ingrese un número romano: ")
                        print(f"Decimal: {Calculadora_NumericoAvanzado.romano_a_decimal(r)}")
                        repetir = input("¿Desea hacer otra conversión Romano a Decimal? (s/n): ").lower()
                        if repetir != "s":
                            break
                elif opcion == 9:
                    Calculadora_NumericoAvanzado.casos_de_prueba()
                elif opcion == 10:
                    print("Saliendo...")
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
                input("Presione Enter para volver al menú...")
        elif opcion == 2:
            if hasattr(fisicas, "main") and callable(fisicas.main):
                fisicas.main()
            elif hasattr(fisicas, "calculadora_fisica") and callable(fisicas.calculadora_fisica):
                fisicas.calculadora_fisica()
            elif hasattr(fisicas, "menu") and callable(fisicas.menu):
                fisicas.menu()
            try:
                sub = int(input("Elige opción de Físicas: "))
                if hasattr(fisicas, "dispatch") and callable(fisicas.dispatch):
                    fisicas.dispatch(sub)
                else:
                    print("El módulo solo expone menu(); agrega main()/dispatch() para interactuar.")
            except ValueError:
                print("Opción inválida.")
            else:
                print("El módulo 'fisicas' no expone main(), calculadora_fisica() ni menu().")


        
        elif opcion == 3:
            print("\n=== Calculadora Digital ===")
            while True:
                print("\n--------- MENÚ DIGITAL ---------")
                print("1. Bytes ↔ Kilobytes")
                print("2. Kilobytes ↔ Megabytes")
                print("3. Megabytes ↔ Gigabytes")
                print("4. bps ↔ Mbps")
                print("5. Mostrar tabla de conversiones (historial ordenado)")
                print("6. Ejecutar pruebas automáticas")
                print("7. Regresar al menú principal")

                op_digital = int(input("Seleccione una opción (1-7): "))

                if 1 <= op_digital <= 4:
                    i = op_digital - 1  
                    calc_digital.mostrar_tipo_conversion(i)

                    u1 = calc_digital.unidades1[i]
                    u2 = calc_digital.unidades2[i]

                    print(f"\nHas elegido convertir entre {u1} y {u2}")
                    print("1.", u1, "→", u2)
                    print("2.", u2, "→", u1)
                    direccion = int(input("Selecciona el sentido de conversión: "))

                    valor = calc_digital.pedir_valor()

                    if calc_digital.confirmacion():
                        calc_digital.animacion_conversion(u1, u2)
                        resultado = calc_digital.convertir(i, direccion, valor)

                        if direccion == 1:
                            print(f"\nResultado: {valor} {u1} equivalen a {resultado} {u2}\n")
                        else:
                            print(f"\nResultado: {valor} {u2} equivalen a {resultado} {u1}\n")

                        texto = f"{u1} ↔ {u2}: {valor} -> {resultado}"
                        calc_digital.guardar_en_archivo(texto)

                    repetir = input("¿Desea hacer otra conversión digital? (s/n): ").lower()
                    if repetir != "s":
                        break

                elif op_digital == 5:
                    calc_digital.tabla_conversiones()

                elif op_digital == 6:
                    calc_digital.pruebas_codigo()

                elif op_digital == 7:
                    print("Regresando al menú principal...\n")
                    break

                else:
                    print("Opción no válida. Intente de nuevo.")

        elif opcion == 4:
            print("----------CONVERSIONES CREATIVAS--------------")
            while True:
                calc_creativas.menu()  # Mostrar menú principal
                opcion = int(input("Elige una opción: "))
        
                # --- Opción 1: Altura en equivalentes de libros ---
                if opcion == 1:
                    while True:
                        print("----------TORRES DE LIBROS----------")
                        print("A cuántos libros equivalen:")
                        altura = calc_creativas.pedir_valor()
                        while altura is None:
                            altura = pedir_valor()
        
                        unidades = ['km', 'm', 'cm', 'mm', 'in', 'ft', 'yd', 'mi']
                        unidad = calc_creativas.pedir_unidad(unidades)
                        while unidad is None:
                            unidad = calc_creativas.pedir_unidad(unidades)
        
                        calc_creativas.altura_libros(altura, unidad)
        
                        repetir = input("¿Desea hacer otra conversión de altura? (s/n): ").lower()
                        if repetir != "s":
                            break
        
                # --- Opción 2: Peso en gatos/gatitos ---
                elif opcion == 2:
                    while True:
                        print("----------PESO EN GATOS Y GATITOS----------")
                        print("A cuántos gatos y gatitos equivale:")
                        peso = calc_creativas.pedir_valor()
                        while peso is None:
                            peso = calc_creativas.pedir_valor()
        
                        unidades = ['ton', 'kg', 'g', 'lb', 'oz', 'slug']
                        unidad = calc_creativas.pedir_unidad(unidades)
                        while unidad is None:
                            unidad = calc_creativas.pedir_unidad(unidades)
        
                        calc_creativas.peso_gatitos(peso, unidad)
        
                        repetir = input("¿Desea hacer otra conversión de peso? (s/n): ").lower()
                        if repetir != "s":
                            break
        
                # --- Opción 3: Energía en barras de chocolate o TNT ---
                elif opcion == 3:
                    while True:
                        print("---------ENERGÍA EN BARRAS DE CHOCOLATE Y TNT---------")
                        print("A cuántas barras o unidades de TNT equivale:")
                        energia = calc_creativas.pedir_valor()
                        while energia is None:
                            energia = calc_creativas.pedir_valor()
        
                        unidades = ['kcal', 'J', 'kJ', 'kWh', 'BTU']
                        unidad = calc_creativas.pedir_unidad(unidades)
                        while unidad is None:
                            unidad = calc_creativas.pedir_unidad(unidades)
        
                        calc_creativas.energia_en_barras(energia, unidad)
        
                        repetir = input("¿Desea hacer otra conversión de energía? (s/n): ").lower()
                        if repetir != "s":
                            break
        
                # --- Opción 4: Volumen a propiedades de un agujero negro ---
                elif opcion == 4:
                    while True:
                        print("-------VOLUMEN A PROPIEDADES DE UN AGUJERO NEGRO-------")
                        print("Un agujero negro de volumen:")
                        volumen = calc_creativas.pedir_valor()
                        while volumen is None:
                            volumen = pedir_valor()
        
                        unidades = ['km', 'm', 'cm', 'mm', 'in', 'ft', 'yd', 'mi', 'l', 'gal']
                        unidad = calc_creativas.pedir_unidad(unidades)
                        while unidad is None:
                            unidad = calc_creativas.pedir_unidad(unidades)
        
                        calc_creativas.vol_agujero_negro(volumen, unidad)
        
                        repetir = input("¿Desea hacer otra conversión de volumen? (s/n): ").lower()
                        if repetir != "s":
                            break
        
                # --- Opción 5: Distancia en equivalentes de animales marinos ---
                elif opcion == 5:
                    while True:
                        print("--------DISTANCIA EQUIVALENTE EN ANIMALES MARINOS-------")
                        print("La distancia es equivalente a:")
                        distancia = calc_creativas.pedir_valor()
                        while distancia is None:
                            distancia = calc_creativas.pedir_valor()
        
                        unidades = ['km', 'm', 'cm', 'mm', 'in', 'ft', 'yd', 'mi']
                        unidad = calc_creativas.pedir_unidad(unidades)
                        while unidad is None:
                            unidad = calc_creativas.pedir_unidad(unidades)
        
                        calc_creativas.distancia_marina(distancia, unidad)
        
                        repetir = input("¿Desea hacer otra conversión de distancia? (s/n): ").lower()
                        if repetir != "s":
                            break
        
                # --- Opción 6: Pruebas rápidas ---
                elif opcion == 6:
                    print("----PRUEBAS DE LAS FUNCIONES CON VALORES POR DEFAULT----")
                    op = calc_creativas.pedir_valor()
                    while op is None:
                        op = calc_creativas.pedir_valor()
        
                    calc_creativas.pruebas(op)
        
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
