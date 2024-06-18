import math
def calcular_raiz_cuadrada(number):
    if number >= 0:
        return math.sqrt(number)
    else:
        return "There is no root a negative number"

number = float(input("Type a number to calculate its square root: "))

result = calcular_raiz_cuadrada(number)
print(result)
