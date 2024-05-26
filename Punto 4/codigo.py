# Función para contar la frecuencia de palabras en una cadena python

def contar_palabras(cadena):
    
    # Convertir la cadena a minúsculas y eliminar los signos de puntuación
    cadena = cadena.lower()
    caracteres_a_eliminar = [',', '.', ';', ':', '!', '?', '(', ')', '[', ']', '{', '}', '-', '_', '"', "'"]
    for caracter in caracteres_a_eliminar:
        cadena = cadena.replace(caracter, ' ')
    
    # Dividir la cadena en palabras
    palabras = cadena.split()
    
    # Crear el diccionario de frecuencias
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    
    return frecuencias

#Función para encontrar la palabra más repetida

def palabra_mas_repetida(frecuencias):
   
    max_palabra = max(frecuencias, key=frecuencias.get)
    max_frecuencia = frecuencias[max_palabra]
    return (max_palabra, max_frecuencia)

#Programa Principal

# Solicita la cadena de caracteres al usuario
cadena = input("Ingrese una cadena de caracteres: ")

# Llama a la función 'contar_palabras' para obtener el diccionario de frecuencias
frecuencias = contar_palabras(cadena)
print("Frecuencia de palabras:")
print(frecuencias)

# Por ultimo, llama a la función 'palabra_mas_repetida' para obtener la palabra más repetida y su frecuencia
palabra_frecuencia = palabra_mas_repetida(frecuencias)
print(f"La palabra más repetida es '{palabra_frecuencia[0]}' con una frecuencia de {palabra_frecuencia[1]}")

