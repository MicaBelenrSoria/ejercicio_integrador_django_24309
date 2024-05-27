# En este sexto ejercicio hay que Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
# siguientes métodos para la clase:
# * Un constructor, donde los datos pueden estar vacíos.
# * Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
#   datos.
# * mostrar(): Muestra los datos de la persona.
# * Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

# Para implementar la clase Persona con los atributos nombre, edad y DNI, y los métodos solicitados en el enunciado lo analice de la siguiente forma:

# 1 - Crear un constructor que inicialice los atributos con valores por defecto.
# 2 - Implementar los métodos setters y getters para cada atributo, con validación de datos.
# 3 - Implementar el método mostrar() para mostrar los datos de la persona.
# 4 - Implementar el método es_mayor_de_edad() para determinar si la persona es mayor de edad.

# Explicacion del desarrollo del codigo

# Constructor ('__init__'):Inicializa los atributos 'nombre', 'edad' y 'DNI' con valores por defecto. Estos valores pueden ser vacíos o cero.

# Getters y Setters:

# Para cada atributo (nombre, edad, dni), se define una propiedad (@property) para obtener el valor y un método setter para establecer el valor.
# Los setters incluyen validaciones para asegurar que los valores proporcionados son válidos:
#       nombre: Debe ser una cadena de caracteres no vacía.
#       edad: Debe ser un número entero positivo.
#       dni: Debe ser una cadena de caracteres no vacía.

# Método mostrar(): Imprime los datos de la persona.

# Método es_mayor_de_edad(): Devuelve 'True' si la edad de la persona es 18 o más, y 'False' en caso contrario.

# Ejemplo de uso:
#   * Se crea una instancia de Persona con valores iniciales.
#   * Se muestran los datos de la persona y se verifica si es mayor de edad.
#   * Se prueban los setters y getters, y se vuelven a mostrar los datos de la persona y su condición de mayor de edad.
