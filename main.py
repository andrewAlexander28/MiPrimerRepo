import math
def calcular_raiz_cuadrada(numero):
    if numero >= 0:
        return math.sqrt(numero)
    else:
        return "There is no root a negative number"

# Pedir al usuario que ingrese un número
numero = float(input("Type a number to calculate its square root: "))

# Calcular y mostrar el resultado
resultado = calcular_raiz_cuadrada(numero)
print(resultado)