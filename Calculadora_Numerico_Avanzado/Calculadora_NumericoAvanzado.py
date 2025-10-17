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
import os
def casos_de_prueba():
    ruta = os.path.join("Calculadora_Numerico_Avanzado", "algoritmo.txt")
    algoritmo = open(ruta, "r")
    algoritmo.seek(0)
    contenido = algoritmo.read()
    print(contenido)
    algoritmo.close()
    


'''Convierte un número decimal (n) a su equivalente en binario, retornando una 
cadena con el número binario.'''
def decimal_a_binario(n):
    if n == 0:
        return "0"
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario
        n = n // 2
    return binario

'''Convierte un número binario (b) en una cadena a su equivalente en decimal, 
retornando un valor entero.'''
def binario_a_decimal(b):
    decimal = 0
    potencia = 0
    for digito in reversed(b):
        decimal += int(digito) * (2 ** potencia)
        potencia += 1
    return decimal

'''Convierte un número decimal (n) a su equivalente en octal, retornando una
cadena con el número octal.'''
def decimal_a_octal(n):
    if n == 0:
        return "0"
    octal = ""
    while n > 0:
        octal = str(n % 8) + octal
        n = n // 8
    return octal

'''Convierte un número octal (o) en una cadena a su equivalente en decimal, 
retornando un valor entero.'''
def octal_a_decimal(o):
    decimal = 0
    potencia = 0
    for digito in reversed(o):
        decimal += int(digito) * (8 ** potencia)
        potencia += 1
    return decimal

'''Convierte un número decimal (n) a su equivalente en hexadecimal, retornando 
una cadena con el número hexadecimal.'''
def decimal_a_hexadecimal(n):
    if n == 0:
        return "0"
    hexadecimales = "0123456789ABCDEF"
    hexadecimal = ""
    while n > 0:
        hexadecimal = hexadecimales[n % 16] + hexadecimal
        n = n // 16
    return hexadecimal

'''Convierte un número hexadecimal (h) en una cadena a su equivalente en decimal, 
retornando un valor entero.'''
def hexadecimal_a_decimal(h):
    hexadecimales = "0123456789ABCDEF"
    decimal = 0
    potencia = 0
    for digito in reversed(h):
        decimal += hexadecimales.index(digito) * (16 ** potencia)
        potencia += 1
    return decimal

'''Convierte un número decimal (n) a su equivalente en números romanos, retornando 
una cadena con el número romano.'''
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

'''Convierte un número romano (r) en una cadena a su equivalente en decimal, 
retornando un valor entero.'''
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
    print("=== MENÚ CALCULADORA NUMÉRICO AVANZADO ===")
    print("\n")
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
