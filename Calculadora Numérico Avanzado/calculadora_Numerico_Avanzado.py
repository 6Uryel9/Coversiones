'''Calculadora de conversiones numéricas entre decimal, binario, octal y hexadecimal.
Fecha: 22-09-2025

Casos de prueba:
1. Decimal a Binario:
   Entrada: 10
   Salida esperada: 1010
2. Binario a Decimal:
   Entrada: 1010
   Salida esperada: 10
3. Decimal a Octal:
   Entrada: 10
   Salida esperada: 12
4. Octal a Decimal:
   Entrada: 12
   Salida esperada: 10
5. Decimal a Hexadecimal:
   Entrada: 255
   Salida esperada: FF
6. Hexadecimal a Decimal:
   Entrada: FF
   Salida esperada: 255
7. Decimal a Romano:
   Entrada: 1994
   Salida esperada: MCMXCIV
8. Romano a Decimal:
   Entrada: XXXIX
   Salida esperada: 39'''

def casos_de_prueba():
    print("Casos de Prueba")
    print("1. Decimal a Binario (10):", decimal_a_binario(10), "-> esperado: 1010")
    print("2. Binario a Decimal (1010):", binario_a_decimal("1010"), "-> esperado: 10")
    print("3. Decimal a Octal (10):", decimal_a_octal(10), "-> esperado: 12")
    print("4. Octal a Decimal (12):", octal_a_decimal("12"), "-> esperado: 10")
    print("5. Decimal a Hexadecimal (255):", decimal_a_hexadecimal(255), "-> esperado: FF")
    print("6. Hexadecimal a Decimal (FF):", hexadecimal_a_decimal("FF"), "-> esperado: 255")
    print("7. Decimal a Romano (1994):", decimal_a_romano(1994), "-> esperado: MCMXCIV")
    print("8. Romano a Decimal (XXXIX):", romano_a_decimal("XXXIX"), "-> esperado: 39")

def decimal_a_binario(n):
    if n == 0:
        return "0"
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario
        n = n // 2
    return binario
def binario_a_decimal(b):
    decimal = 0
    potencia = 0
    for digito in reversed(b):
        decimal += int(digito) * (2 ** potencia)
        potencia += 1
    return decimal
def decimal_a_octal(n):
    if n == 0:
        return "0"
    octal = ""
    while n > 0:
        octal = str(n % 8) + octal
        n = n // 8
    return octal
def octal_a_decimal(o):
    decimal = 0
    potencia = 0
    for digito in reversed(o):
        decimal += int(digito) * (8 ** potencia)
        potencia += 1
    return decimal
def decimal_a_hexadecimal(n):
    if n == 0:
        return "0"
    hexadecimales = "0123456789ABCDEF"
    hexadecimal = ""
    while n > 0:
        hexadecimal = hexadecimales[n % 16] + hexadecimal
        n = n // 16
    return hexadecimal
def hexadecimal_a_decimal(h):
    hexadecimales = "0123456789ABCDEF"
    decimal = 0
    potencia = 0
    for digito in reversed(h):
        decimal += hexadecimales.index(digito) * (16 ** potencia)
        potencia += 1
    return decimal
def decimal_a_romano(n):
    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]
    romano = ""
    for valor, simbolo in valores:
        while n >= valor:
            romano += simbolo
            n -= valor
    return romano
def romano_a_decimal(r):
    valores = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    decimal = 0
    i = 0
    while i < len(r):
        if i + 1 < len(r) and valores[r[i]] < valores[r[i + 1]]:
            decimal += valores[r[i + 1]] - valores[r[i]]
            i += 2
        else:
            decimal += valores[r[i]]
            i += 1
    return decimal
def menu():
    print("1. Decimal a Binario")
    print("2. Binario a Decimal")
    print("3. Decimal a Octal")
    print("4. Octal a Decimal")
    print("5. Decimal a Hexadecimal")
    print("6. Hexadecimal a Decimal")
    print("7. Decimal a Romano")
    print("8. Romano a Decimal")
    print("9. Casos de Prueba")
    print("10. Salir")

def main_calc_A():
    while True:
        menu()
        opcion = int(input("Seleccione una opción (1-9): "))
        if opcion == 1:
            while True:
                n = int(input("Ingrese un número decimal: "))
                print(f"Binario: {decimal_a_binario(n)}")
                repetir = input("¿Desea hacer otra conversión Decimal a Binario? (s/n): ").lower()
                if repetir != "s":
                    break
        elif opcion == 2:
            while True:
                b = input("Ingrese un número binario: ")
                print(f"Decimal: {binario_a_decimal(b)}")
                repetir = input("¿Desea hacer otra conversión Binario a Decimal? (s/n): ").lower()
                if repetir != "s":
                    break
        elif opcion == 3:
            while True:
                n = int(input("Ingrese un número decimal: "))
                print(f"Octal: {decimal_a_octal(n)}")
                repetir = input("¿Desea hacer otra conversión Decimal a Octal? (s/n): ").lower()
                if repetir != "s":
                    break
        elif opcion == 4:
            while True:
                o = input("Ingrese un número octal: ")
                print(f"Decimal: {octal_a_decimal(o)}")
                repetir = input("¿Desea hacer otra conversión Octal a Decimal? (s/n): ").lower()
                if repetir != "s":
                    break
        elif opcion == 5:
            while True:
                n = int(input("Ingrese un número decimal: "))
                print(f"Hexadecimal: {decimal_a_hexadecimal(n)}")
                repetir = input("¿Desea hacer otra conversión Decimal a Hexadecimal? (s/n): ").lower()
                if repetir != "s":
                    break
        elif opcion == 6:
            while True:
                h = input("Ingrese un número hexadecimal: ")
                print(f"Decimal: {hexadecimal_a_decimal(h)}")
                repetir = input("¿Desea hacer otra conversión Hexadecimal a Decimal? (s/n): ").lower()
                if repetir != "s":
                    break
        elif opcion == 7:
            while True:
                n = int(input("Ingrese un número decimal: "))
                print(f"Romano: {decimal_a_romano(n)}")
                repetir = input("¿Desea hacer otra conversión Decimal a Romano? (s/n): ").lower()
                if repetir != "s":
                    break
        elif opcion == 8:
            while True:
                r = input("Ingrese un número romano: ")
                print(f"Decimal: {romano_a_decimal(r)}")
                repetir = input("¿Desea hacer otra conversión Romano a Decimal? (s/n): ").lower()
                if repetir != "s":
                    break
        elif opcion == 9:
            casos_de_prueba()
        elif opcion == 10:
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        input("Presione Enter para volver al menú...")
main_calc_A()
