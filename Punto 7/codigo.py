class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._nombre = valor
        else:
            raise ValueError("El nombre debe ser una cadena de caracteres no vacía.")

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if isinstance(valor, int) and valor >= 0:
            self._edad = valor
        else:
            raise ValueError("La edad debe ser un número entero positivo.")

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._dni = valor
        else:
            raise ValueError("El DNI debe ser una cadena de caracteres no vacía.")

    def mostrar(self):
        print(f"Nombre: {self._nombre}")
        print(f"Edad: {self._edad}")
        print(f"DNI: {self._dni}")

    def es_mayor_de_edad(self):
        return self._edad >= 18


class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        
        self._titular = titular
        self._cantidad = cantidad

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, valor):
        if isinstance(valor, Persona):
            self._titular = valor
        else:
            raise ValueError("El titular debe ser una instancia de la clase Persona.")

    @property
    def cantidad(self):
        return self._cantidad

    def mostrar(self):
        
        print("Datos de la cuenta:")
        self._titular.mostrar()
        print(f"Cantidad: {self._cantidad}")

    def ingresar(self, cantidad):
       
        if cantidad > 0:
            self._cantidad += cantidad

    def retirar(self, cantidad):
        
        self._cantidad -= cantidad


# Ejemplo de uso
titular = Persona("Juan Pérez", 30, "12345678")
cuenta = Cuenta(titular, 1000.0)
cuenta.mostrar()
cuenta.ingresar(500)
print("\nDespués de ingresar 500:")
cuenta.mostrar()
cuenta.retirar(200)
print("\nDespués de retirar 200:")
cuenta.mostrar()
