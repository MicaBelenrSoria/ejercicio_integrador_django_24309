# En este quinto ejercicio dice que . Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.

# Entonces para este ejercicio necesito crear una función llamada get_int() que solicite al usuario un valor entero y lo devuelva, iterando hasta que el usuario proporcione un valor válido. 
# Y además, se requiere implementar tanto una solución iterativa como una solución recursiva.

"""
    Solicita al usuario un valor entero y lo devuelve.
    Recursivamente llama a sí misma hasta que se proporcione un valor válido.
    
    Retorna:
    int: El valor entero proporcionado por el usuario.
    """

# Solución Iterativa:

# En la función 'get_int()' utiliza un bucle while True para solicitar al usuario un valor entero.
# Luego dentro del bucle, intenta convertir la entrada del usuario en un entero.
# Si se lanza una excepción 'ValueError', muestra un mensaje de error y continúa solicitando al usuario un valor entero válido.
# Si la conversión se puede realizar, se devuelve el valor entero ingresado por el usuario y sale del bucle.

# Solución Recursiva:

# En la función 'get_int()' utiliza una estructura de control 'try-except' para manejar la conversión a entero.
# Si se lanza una excepción 'ValueError', muestra un mensaje de error y llama recursivamente a sí misma para solicitar al usuario un nuevo valor entero válido.
# Si la conversión se puede realizar, devuelve el valor entero ingresado por el usuario.