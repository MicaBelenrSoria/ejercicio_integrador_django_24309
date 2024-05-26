def calcular_mcm(a, b):
   
    def mcd(x, y):
        while y:
            x, y = y, x % y
        return x

    return abs(a * b) // mcd(a, b)

# Números proporcionados directamente en el código
numero1 = 15
numero2 = 20
mcm = calcular_mcm(numero1, numero2)
print(f"El MCM de {numero1} y {numero2} es {mcm}")
