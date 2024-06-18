import math
def calculate_square_root(number):
    if number >= 0:
        return math.sqrt(number)
    else:
        return "There is no root a negative number"

number = float(input("Type a number to calculate its square root: "))

result = calculate_square_root(number)
print(result)
