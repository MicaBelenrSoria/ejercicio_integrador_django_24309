def calcular_mcm(a, b):
    
    def mcd(x, y):
        while y:
            x, y = y, x % y
        return x

    return abs(a * b) // mcd(a, b)

# Solicitar números al usuario
numero1 = int(input("Ingrese el primer número por favor: "))
numero2 = int(input("Ingrese el segundo número por favor: "))
mcm = calcular_mcm(numero1, numero2)
print(f"El MCM de {numero1} y {numero2} es {mcm}")
