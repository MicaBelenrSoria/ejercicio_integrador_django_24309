# Solución Iterativa

def get_int():
    
    while True:
        try:
            valor = int(input("Ingrese un valor entero: "))
            return valor
        except ValueError:
            print("Error: ¡Debe ingresar un valor entero válido!")

# Ejemplo de uso
valor_entero = get_int()
print("El valor entero ingresado es:", valor_entero)

# Solucion Recursiva 

def get_int():
    
    try:
        valor = int(input("Ingrese un valor entero: "))
        return valor
    except ValueError:
        print("Error: ¡Debe ingresar un valor entero válido!")
        return get_int()  # Llamada recursiva

# Ejemplo de uso
valor_entero = get_int()
print("El valor entero ingresado es:", valor_entero)

