def calcular_mcd(a, b):
    
    while b:
        a, b = b, a % b
    return a

# Solicitar números al usuario para que luego de como salida MCD
numero1 = int(input("Ingrese el primer número por favor: "))
numero2 = int(input("Ingrese el segundo número por favor: "))
mcd = calcular_mcd(numero1, numero2)
print(f"El MCD de {numero1} y {numero2} es {mcd}")