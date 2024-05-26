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

# Solicitar la cadena de caracteres al usuario
cadena = input("Ingrese una cadena de caracteres: ")
frecuencias = contar_palabras(cadena)
print("Frecuencia de palabras:")
print(frecuencias)


