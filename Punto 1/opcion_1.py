def calcular_mcd(a, b):

    while b:
        a, b = b, a % b
    return a

# Números proporcionados directamente en el codigo 
numero1 = 45
numero2 = 8
mcd = calcular_mcd(numero1, numero2)
print(f"El MCD de {numero1} y {numero2} es {mcd}")
