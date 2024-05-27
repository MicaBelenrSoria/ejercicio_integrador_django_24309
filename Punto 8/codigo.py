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


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self._bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self._bonificacion

    @bonificacion.setter
    def bonificacion(self, valor):
        if isinstance(valor, (int, float)) and 0 <= valor <= 100:
            self._bonificacion = valor
        else:
            raise ValueError("La bonificación debe ser un número entre 0 y 100.")

    def es_titular_valido(self):
        return 18 <= self._titular.edad < 25

    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print(f"Bonificación: {self._bonificacion}%")

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("El titular no es válido para retirar dinero de la Cuenta Joven.")


# Ejemplo de uso
titular = Persona("Ana López", 22, "87654321")
cuenta_joven = CuentaJoven(titular, 1000.0, 10.0)
cuenta_joven.mostrar()

# Ingresar y retirar dinero
cuenta_joven.ingresar(500)
print("\nDespués de ingresar 500:")
cuenta_joven.mostrar()

cuenta_joven.retirar(200)
print("\nDespués de retirar 200:")
cuenta_joven.mostrar()

# Intentar retirar con titular no válido
titular_no_valido = Persona("Juan Pérez", 30, "12345678")
cuenta_joven_no_valida = CuentaJoven(titular_no_valido, 1000.0, 10.0)
cuenta_joven_no_valida.mostrar()
cuenta_joven_no_valida.retirar(100)


