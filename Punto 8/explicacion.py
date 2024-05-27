# En este octavo ejercicio hay que Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
# CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
# además del titular y la cantidad se debe guardar una bonificación que estará expresada en
# tanto por ciento. Crear los siguientes métodos para la clase:

# * Un constructor.
# * Los setters y getters para el nuevo atributo.
# * En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
#   tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
#   mayor de edad pero menor de 25 años y falso en caso contrario.
# * Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
# * El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
#   cuenta.

# Hay que crear la clase CuentaJoven derivada de Cuenta, agregaremos un nuevo atributo bonificación y extenderemos o modificaremos algunos métodos.

# Explicacion de mi codigo:

# 1 - Clase Persona: Ya se ha definido previamente.

# 2 - Clase Cuenta: Ya se ha definido previamente.

# 3 - Clase CuentaJoven:

#     - Constructor (__init__): Inicializa titular, cantidad y el nuevo atributo bonificación. Llama al constructor de la clase base (Cuenta) utilizando super().
#     - Propiedades (@property):
#           * bonificacion: Getter y setter para el atributo bonificación, con validación para asegurar que sea un valor entre 0 y 100.
#     - Método es_titular_valido(): Verifica si el titular es mayor de edad pero menor de 25 años.
#     - Método mostrar(): Muestra "Cuenta Joven" y la bonificación, además de llamar al método mostrar() de la clase base para mostrar los datos de la cuenta y el titular.
#     - Método retirar(cantidad): Solo permite retirar dinero si el titular es válido (mayor de edad pero menor de 25 años). Si no es válido, muestra un mensaje indicando que no puede retirar dinero.

# Ejemplo de uso:
# * Se crea una instancia de Persona para el titular válido y otra para un titular no válido.
# * Se crea una instancia de CuentaJoven con un titular válido y se realizan operaciones de ingreso y retiro de dinero.
# * Se muestra cómo se maneja la situación cuando se intenta retirar dinero con un titular no válido.
