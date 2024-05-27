# En este septimo ejercicio hay que Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
# persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
# opcional. Crear los siguientes métodos para la clase:
#   * Un constructor, donde los datos pueden estar vacíos.
#   * Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
#     directamente, sólo ingresando o retirando dinero.
#   * mostrar(): Muestra los datos de la cuenta.
#   * ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
#     negativa, no se hará nada.
#   * retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
#     rojos.

# Entonces hay qu crear la clase Cuenta con los atributos titular y cantidad, y los métodos que furon mencionados en el enunciado:

# 1 - Crear un constructor que inicialice los atributos con valores por defecto.
# 2 - Implementar los métodos setters y getters para cada atributo, con las restricciones mencionadas.
# 3 - Implementar el método mostrar() para mostrar los datos de la cuenta.
# 4 - Implementar los métodos ingresar(cantidad) y retirar(cantidad) para gestionar las operaciones de la cuenta.

# Entonses lo desarrolle de la siquiente manera

# Clase Persona: Se incluye nuevamente la clase Persona para completar el ejemplo, dado que titular debe ser una instancia de Persona.

# Clase Cuenta:
#   * Constructor (__init__):Inicializa titular como una instancia de Persona y cantidad como un valor opcional (por defecto 0.0).
#   * Propiedades (@property):
#       - titular: Se verifica que el valor asignado sea una instancia de Persona.
#       - cantidad: Solo se proporciona el getter, ya que no se permite la modificación directa del valor.
#   * Método mostrar():Muestra los datos de la cuenta, incluyendo la información del titular y la cantidad.

#   * Método ingresar(cantidad):Ingresa una cantidad a la cuenta, siempre que sea positiva.
#   * Método retirar(cantidad):
#   * Retira una cantidad de la cuenta, permitiendo que la cuenta tenga saldo negativo.

# Ejemplo de uso:
#   - Se crea una instancia de Persona para el titular.
#   - Se crea una instancia de Cuenta con el titular y una cantidad inicial.
#   - Se muestran los datos de la cuenta, se realizan operaciones de ingreso y retiro de dinero, y se muestran los resultados después de cada operación. 