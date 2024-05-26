# En este tercer ejecicio hay que escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

"""
    Se recibe una cadena de caracteres y devuelve un diccionario con cada palabra
    y la cantidad de veces que aparece en la cadena.

    Parámetros:
    cadena (str): La cadena de caracteres.

    Retorna:
    diccionario: Un diccionario con la frecuencia de cada palabra.
    """

# EXPLICACION DEL CODIGO QUE REALICE ES:

# Función 'contar_palabras':

# * Recibe una cadena de caracteres y devuelve un diccionario con la frecuencia de cada palabra.
# * Convierte la cadena a minúsculas para que la frecuencia no sea sensible a mayúsculas/minúsculas.
# * Elimina los signos de puntuación para considerar solo las palabras.
# * Divide la cadena en palabras utilizando split().
# * Recorre las palabras y actualiza el diccionario frecuencias con la cantidad de veces que aparece cada palabra.

# Solicitar la cadena de caracteres al usuario:

# Usa input() para solicitar la cadena de caracteres al usuario.
# Llama a la función contar_palabras con la cadena ingresada.
# Imprime el diccionario resultante con la frecuencia de palabras.
